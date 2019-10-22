#FORMULACION RECURSIVA

a=int(input("Ingrese la posición del numero a buscar"))

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


print(fib(a))