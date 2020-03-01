archivo = open("archivoDePrueba.txt","w")
lista = [1,2,3,4,5,6,7,8,9,0,9,8,7,6,5,4]
for i in range(len(lista)):
    print(lista[0])
    lista.pop(0)
print(lista)