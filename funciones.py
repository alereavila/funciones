def contadorIncremento (numero):
    for contar in range(0,numero+1,4):
        print(contar)
def calculaAreaTriangulo(base,altura):
    return base*altura/2



numero=int(input("numero para contar :  "))
contadorIncremento(numero)
unaBase=float(input("Introduce la base:  "))
unaAltura=float(input("Introduce la altura:  "))
print(f"El area es: {calculaAreaTriangulo(unaBase,unaAltura)}")