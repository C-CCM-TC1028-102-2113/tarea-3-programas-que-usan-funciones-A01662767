
def tarjeta (a, b):
    resultado = (a * 12) + (b * 35) 
    return (resultado)

def main():
    #escribe tu código abajo de esta línea
 num1 = int(input("INTRODUCE LOS PLIEGOS DE PAPEL: "))
 num2 = int(input("INTRODUCE LAS PLUMAS: "))

 print ("EL NUMERO MAXIMO DE TTARJETAS QUE SE PUEDEN HACER SON: ", tarjeta (num1, num2))

pass


if __name__ == '__main__':
    main()
