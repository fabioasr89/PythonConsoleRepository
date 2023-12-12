#creare una lista contenente 20 interi random in [0, 100)
# e stampare il numero di elementi pari, il numero di elementi maggiori di 70,
#  media e varianza degli elementi

import random


number=[];
i=0;
p=0;
total=100;
while i<total:
    p=random.randint(0,total)
    if p not in number :
        number.append(p)
        i+=1

i=0;
somma=0
numeriMagg70=[]
varianza=0
for p in number:
    somma=somma+p
    if p>70:
        numeriMagg70.append(p)
    if p%2==0:
        i+=1
media=somma/total
##Calcolo varianza
somma=0;
for p in number:
    somma=somma+((p-media)*(p-media))

varianza=somma/total
print("************************ STAMPA NUMERI MAGGIORI DI 70 **********************\n\n")    
print("Numeri naturali maggiori di 70 e inseriti nella lista:\n")
print(numeriMagg70)
print("************************ STAMPA ELEMENTI PARI DELLA LISTA **************************\n\n")    
print("Numero elementi pari:"+str(i))
print("************************CALCOLO MEDIA ARITMETICA*************************************\n\n")    
print("Media aritmetica:"+str(i))
print("************************VARIANZA*************************************\n\n")    
print("Varianza:"+str(varianza))



  
   
   
       
       
    
  
       
      
      
        
  
  