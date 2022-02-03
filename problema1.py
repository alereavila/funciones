def serieFibonacci(limite):
    """
    AQUI DEBERÍA DE ESTAR LA DOCUMENTACION

    """
    a,b=0,1
    while a < limite:
        print(a," ",end="")
        a,b=b,a+b
    print()
if __name__=="__main__":
    numero=int(input("Ingresa un numero limite de la serie de Fibunacci:  "))
    serieFibonacci(numero)
