#Scrivere un algoritmo che generi una matrice di dimensioni fissate in input dall'utente, e tale
#che gli elementi che la costituiscono siano distinti due a due. Il programma dovrà chiedere anche all'utente anche il range dei numeri
#che compariranno tra gli elementi della stessa e controllare che tale intervallo sia compatibile con la dimensione

from random import randint
import numpy as numpy

print("Benvenuto")
check=0
numeroRighe=0
numeroColonne=0
estremoInferiore=0
estremoSuperiore=0
while check==0:
    try:
        numeroRighe=int(input("Quante righe deve avere la matrice?"))
        numeroColonne=int(input("Quante colonne deve avere la matrice"))
        estremoInferiore=int(input("Definire l'estremo inferiore degli elementi della matrice"))
        estremoSuperiore=int(input("Definire l'estremo superiore degli elementi della matrice"))
        numElementi=numeroRighe*numeroColonne
        capacita=estremoSuperiore-estremoInferiore
        if capacita>=numElementi:
            check=1
        else:
            print("Attenzione, la capacita della matrice e' "+str(capacita)+" , e non e' sufficiente per gestire un numero di elementi pari a "+str(numElementi))
    except:
            check=0
    
def generaMatriceUnivoca(numRighe,numColonne,min,max):
    number=[]
    numElementi=numColonne*numRighe
    i=0
    while i<numElementi:
        n=randint(min,max);
        if n not in number:
            number.append(n)
            i+=1
    print("Costruzione matrice in corso...")
    matrix=numpy.zeros((numeroRighe,numeroColonne))
    column=0
    row=0
    print("Size number:"+str(len(number)))
    print(number)
    for element in number:
         if column<=(numeroColonne-1):
              print("Row:"+str(row)+", Colonna:"+str(column)) 
              column+=1 
         elif column>(numeroColonne-1):
              row+=1
              column=0
         matrix[row][column]=element
         
    print("Matrice correttamente generata")
    return matrix

print("Stampa in corso della matrice...\n")
print(generaMatriceUnivoca(numeroRighe,numeroColonne,estremoInferiore,estremoSuperiore))