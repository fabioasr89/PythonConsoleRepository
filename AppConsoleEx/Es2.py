#2 leggere da tastiera una sequenza di interi (la lunghezza è data anch'essa da tastiera), 
#memorizzarla in una lista, verificare se la sequenza è in ordine non decrescente

lunghezza=int(input("Ciao, definisci la lunghezza della sequenza di interi che vuoi creare"))
print("La lunghezza che hai definito vale:"+str(lunghezza))
i=0
number=[]
app=0
while i<lunghezza:
       try: 
            app=int(input("Inserire un numero:"))
            if app:
                number.append(app)
                i=i+1
       except:
            print("Attenzione, l'elemento deve essere un numero intero")
            
prec=0
count=0
check=bool(True)
for p in number:
   if count>0 and p<prec:
        check=bool(False)
        break
   prec=p
   count+=1

if check:
    print("Sequenza inserita in ordine non decrescente") 
else:
    print("Sequenza  inserita non in ordine non decrescente") 
     
        
