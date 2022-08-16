lista = []

print ("¡Bienvenido Usuario!")

for i in range(0,5):
    lista.append(int(input("Ingrese un numero por favor: ")))


print("Su lista de numeros es: ", lista)

# Suma de los numeros ingresados
def sumar(lista):
    num = 0
    for i in range(len(lista)):
        num += lista[i]
    return num

resultado= sumar(lista)
print("El resultado de la suma es:", resultado)

# Calcula el Promedio 
def promedio(lista):
    return sumar(lista)/len(lista)

prom = promedio(lista)
print("El promedio de los numeros es: ", prom)

# Buscamos el valor maximo de los numeros de la lista
def maximo(lista):
    max = lista [0]
    for z in lista:
        if z > max :
            max = z 
    return max 

max = maximo(lista)
print("El máximo de los valores es:", max)

#Buscamos el valor minimo de los numeros ingresados
def minimo(lista):
    min = lista [0]
    for z in lista:
        if z < min:
            min = z
    return min
min = minimo(lista)
print("El minimo de los valores es: ", min)
  

print("Muchas gracias, Adios")