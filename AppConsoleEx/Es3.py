#funzione che, dato n, restituisce la lista dei primi n numeri della successione di Fibonacci
#versione ricorsiva listaFibonacciRicorsiva.py
#versione iterativa listaFibonacciIterativa.py


n=int(input("Inserisci la lunghezza della lista dei primi numeri di fibonacci che vuoi che il sistema calcoli:"))


def fibonacci(n):
    number=[]
    position=0
    if n>0:
        app=0
        fibonacci=0
        for p in range(0,n):
            if p<=1:
                fibonacci=1
            elif p>1:
                 i=position 
                 fibonacci=number[i-1]+number[i-2]
            app=p
            number.append(fibonacci)
            position+=1
    return number

print("Fibonacci lista iterativa:\n")
print(fibonacci(n))
fibonacciList=[]
def fibonacciRicorsiva(n):
    number=[]
    fibonacci=0
    if n<=1:
        fibonacci=1
    elif n>1:
        fibonacci=fibonacciRicorsiva(n-1)+fibonacciRicorsiva(n-2)
    return fibonacci

print("Fibonacci ricorsiva:\n")
fibN=fibonacciRicorsiva(n)
for p in range(0,n):
    fibonacciList.append(fibonacciRicorsiva(p))
    
print(fibonacciList)