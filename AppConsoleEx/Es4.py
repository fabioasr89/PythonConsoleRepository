#4 Leggere da input una sequenza di numeri, e restiuire due liste con gli elementi ordinati
#in modo crescente e decrescente



i=0
lunghezza=0
while i==0:
    try:
        lunghezza=int(input("Quanti numeri vuoi inserire?"))
        i=1
    except:
        i=0
i=0
number=[]
while i<lunghezza:
    try:
        p=int(input("Inserisci numero:"))
        number.append(p)
        i+=1
    except:
        print("Errore, inserisci un numero")
   

def ordina(lista,p):
    if len(lista)>0:
        curr=0
        prec=0
        print(str(lista[len(lista)-1]))
        for n in range(0,len(lista)):
            print(str(n))
            for i in range(n,len(lista)):
                if lista[n]>lista[i] and p=="crescente":
                    print("n="+str(n)+",i="+str(i)+",Scambio elementi tra "+str(lista[n])+" e "+str(lista[i])+", lista corrente:"+str(lista))
                    curr=lista[n]
                    app=lista[i]
                    lista[n]=app
                    lista[i]=curr
                elif lista[n]<lista[i] and p=="decrescente":
                    print("n="+str(n)+",i="+str(i)+",Scambio elementi tra "+str(lista[n])+" e "+str(lista[i])+", lista corrente:"+str(lista))
                    curr=lista[n]
                    app=lista[i]
                    lista[n]=app
                    lista[i]=curr
    return lista

print("Lista ordinata in modo crescente:\n")
print(ordina(number,"crescente"))
print("Lista ordinata in modo decresente:\n")
print(ordina(number,"decrescente"))

