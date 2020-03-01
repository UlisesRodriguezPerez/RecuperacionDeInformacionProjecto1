import webbrowser
import os
from bs4 import BeautifulSoup   #pip3 install bs4
from unicodedata import normalize
import requests                 #pip install requests
import urllib.request
import re
import string
import codecs

def extraerArchivosHtmDelDirectorio():

            #Esta lista es la encargada de almacenar las direcciones de cada archivo htm.
    global listaDeDirecciones
    listaDeDirecciones = [] 

            #La variable directorio contiene la direccion de la carpeta Geografía.
    directorio = r'C:\\Users\ulirp\Dropbox\Documentos TEC\III semestre\Recuperación de información textual\Proyectos\TP1\Geografia'
    

            #Este for se encarga de recorrer el directorio en busca de carpetas.
    cont = 0
    for carpeta, subCarpetas, archivos in os.walk(directorio):
        #print('Directorio encontrado: %s' % carpeta)
        #print(subCarpetas)


            #Con este for logramos recorrer cada carpeta en busca de archivos HTM y agregarlos a la listaDeDirecciones.
        for archivo in archivos:

            #print('\t%s' % archi)


                #La variable dreccionDeArchivo es la que contendrá la direccion en perfecto formato para poder leer cada archivo HTM.
                #Sumando en ella la direccion de carpetas, mas la de cada subcarpeta y por ultimo el archivo.
            direccionDeArchivosHtm = f"{carpeta}" + f"{subCarpetas}" + f"{archivo}"

                #Se reemplazan los [] por un -> \ <- ya que con algunas subcarpetas corresponde a vacío. 
            direccionDeArchivosHtm = direccionDeArchivosHtm.replace("[]","\\")

                #Se agrega cada dirección a la lista de direcciones.
            listaDeDirecciones += [direccionDeArchivosHtm]
            

    #print(listaDeDirecciones)


def leerDocumentoHtm():
    global variableTexto
    global coleccion
    coleccion = " "
    for i in range(len(listaDeDirecciones)):
        archivoHtm = listaDeDirecciones[i]

        #path = f"{listaDeDirecciones[i]}"            #r"C:\\Users\ulirp\Dropbox\Documentos TEC\III semestre\Recuperación de información textual\Proyectos\TP1\Geografia\América\Estados_soberanos\f{dirDePrueba}"
        path = f"{listaDeDirecciones[138]}"
        file = codecs.open(path,"rb")
        file1=file.read()
        file1=str(file1)
        html = file1

                        #Se optiene el texto html#
        soup = BeautifulSoup(html) 

                        #Variable encargada de almacenar el texto#
        variableTexto = soup.get_text()
        coleccion += variableTexto
        break #********************************************************************
        #*********************************************************************

        

                #Función que se encargará de eliminar todas las tíldes de cada palabra.
def eliminarTildesAndMayusculas():

        #La variable textoSinMayusculasNiMinusculas será la que contendrá la colección sin minúsculas ni tildes.
    global textoSinMayusculasNiMinusculas
    textoSinMayusculasNiMinusculas = coleccion.lower()
    
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    textoSinMayusculasNiMinusculas = textoSinMayusculasNiMinusculas.translate(trans)
    #print(textoSinMayusculasNiMinusculas)

        #Esta función reemplaza cada signo de puntuación por un espacio, para al final contar las palabras más fácil.
def removerSignosDePuntuacion(textoSinMayusculasNiMinusculas, replace):
    global textoSinSignosDePuntuacion
    textoSinSignosDePuntuacion = re.sub('[%s]' % re.escape(string.punctuation), replace, textoSinMayusculasNiMinusculas)
    print(string.punctuation)


        #Esta función elimina los números de toda la colección.
def removerNumeros():
    import re

        #Esta variable se encargará de contener toda la coleccion sin numeros.
    global textoSinNumeros
    textoSinNumeros = textoSinSignosDePuntuacion
    textoSinNumeros = re.sub("\d", " ", textoSinNumeros)



        #Esta función separa las palabras.
def separarPalabras():
    interruptor = 1
    global listaDePalabras
    global listaControlDePalabras
    listaDePalabras = []#La lista que contendrá todas las palabras.
    listaControlDePalabras = [] #Esta lista será la que contenga el registro o control de cada palabra.
    
                                        #Este for separará cada palabra y lo agregará a la lista.#
    for palabras in textoSinNumeros.split():  
        listaDePalabras.append(palabras)


                                        #Seccion para poder agrupar palabras y llevar un control de ellas.#
    if(interruptor == 1):
        listaDePalabrasTemporal = []
        listaDePalabrasTemporal = listaDePalabras
        for palabraPorCompara in range(len(listaDePalabrasTemporal)):#Optiene la posicion de cada palabra para entonces proceder a 
                                                                #calcular cuando se repite.

            if(listaControlDePalabras):#En caso de la lista no estar vacía entonces continua con las demás instrucciones.
                bandera = 0 #Esta variable bandera se utilizará para distinguir cuando una palabra ya se ha repetido.
                
                for palabraYaCalculada in range(len(listaControlDePalabras)):#Este for se encargará de recorrer la lista (la cual comienza
                                #vacía) y en la cual se irán agregando las palabras que aún no se han repetido o que no se 
                                #encuentran aún en la lista.
                                                            

                                        #Este if se encarga de comparar la palabra de la lista de palabras totales, con
                                    #las palabras de la lista de palabras controladas (En la que no pueden haber repetidas)#
                    if (listaDePalabrasTemporal[palabraPorCompara] == listaControlDePalabras[palabraYaCalculada][1]):

                        listaControlDePalabras[palabraYaCalculada][0] += 1 #En caso de que ambas palabras sean iguales, unicamente se le 
                                        # sumará 1 al registro de esa palabra, porque significa que está repetida.#

                        bandera = 1 # Y se iguala la bandera a 1 para indicar que si se encontraba ya en el texto.
                        #listaDePalabrasTemporal.pop(0)
                        break



                                    #Cuando la bandera sigue en 0 y no en 1, significa que la palabra no se encuentra aún en la lista 
                                    #de palabras controladas, por lo tanto se procede con las demás intrucciones para agregarla a la lista.
                if(bandera == 0):
                    listaControlDePalabras += [[1,listaDePalabrasTemporal[palabraPorCompara]]] #Se agrega la palabra a la lista con un 
                                                #un registro inicial de 1 palabra.
                    #listaDePalabrasTemporal.pop(0)


                                            #Este else es unicamente para agregar la primer palabra, ya que la lista se encontraba
                                            #vacía.#                         
            else:
                listaControlDePalabras += [[1,listaDePalabrasTemporal[palabraPorCompara]]]
                #listaDePalabrasTemporal.pop(0)



            #Esta funcion se encarga de ordenar las palabras alfabeticamente.
def ordenarPalabrasAlfabeticamente():
                #Esta es la lista de palabras ordenadas por abecedario.
    global listaDePalabrasOrdenadasAlfabeticamente
    listaDePalabrasOrdenadasAlfabeticamente = sorted(listaDePalabras)  
    global totalDePalabras           
    totalDePalabras = (len(listaDePalabrasOrdenadasAlfabeticamente))


def ordenarPalabrasPorCantidadDeApariciones():
    global listaDePalabrasOrdenadasPorCantidadDeApariciones
    listaDePalabrasOrdenadasPorCantidadDeApariciones = sorted(listaControlDePalabras)




def consultarPalabra():
    print("Ingrese la palabra que desea consultar: ")
    palabraPorConsultar = input()
    print("\n")

                                        #Forma 1 de imprimir la cantidad de cada letra.#
    #cantidadDeVeces = listaDePalabras.count(palabraPorConsultar)
    #print("La palabra ->" , palabraPorConsultar , "<- aparece " , cantidadDeVeces , "de veces\n")
    #print("En un total de" , len(listaDePalabras) , "palabras\n\n")



                                        #Forma 2 con la lista ya generada con sus respectivos valores.#

                            #Este for se encarga de recorrer la lista de palabras controladas(Con su respectivo conteo)
                            #y poder buscar la palabra solicitada por el usuario.#

    bandera = 0 #Esta bandera se utilizará para saber si se encuentra o no la palabra solicitada por el usuario.
    for i in range(len(listaControlDePalabras)):

        if( palabraPorConsultar == listaControlDePalabras[i][1]):#Cuando se encuentra la palabra se le muestras los resultados al usuario.

            print("La palabra ->",palabraPorConsultar,"<- se repite",listaControlDePalabras[i][0],"veces en el texto.\n")
            aparicionesPorLetra = listaControlDePalabras[i][0]  #Para despues obtener la probabilidad.
            bandera= 1

                #En caso de que la bandera sea uno, significa que la palabra si se encontró y se ejecutan las demás instrucciones.#
    if (bandera == 1):
        print("Hay ->", i+1,"<- palabras diferrentes\n")
        print("Y en total hay ->",len(listaDePalabras),"<- palabras en el texto.\n\n")
        print("Por lo tanto hay un",aparicionesPorLetra/(len(listaDePalabras)),
        "porciento de probabilidad de que salga esta palabra aletoriamente\n")

                #En caso de que la bandera sea igual a 0, significa que la palabra no se encuentra en el texto.
                   # Por lo tanto se le informará al usuario.#
    else:
        print("La palabra que desea consultar no se encuentra en el texto.")
           

 
    #print(listaDePalabrasOrdenadasAlfabeticamente)
    



def calcularProbabilidadDeLasMasAparecidas():
    #ordenarPalabrasAlfabeticamente()
    ordenarPalabrasPorCantidadDeApariciones()
                    #En este if se calcula la cantidad de datos a mostrar en caso que sean más de 100.#
    if (len(listaDePalabrasOrdenadasPorCantidadDeApariciones) > 99):
        largoDeListaOrdenada = len(listaDePalabrasOrdenadasPorCantidadDeApariciones)*0.0008
        largoDeListaOrdenada = int(float(largoDeListaOrdenada))
        print("\nLas siguientes estadíticas son de las",largoDeListaOrdenada, "palabras más aparecidas en el texto.")

                    #En este if se calcula la cantidad de datos a mostrar en caso que sean más de 10 y menos de 100.#
    if(len(listaDePalabrasOrdenadasPorCantidadDeApariciones) > 10 and len(listaDePalabrasOrdenadasPorCantidadDeApariciones) < 99):
        largoDeListaOrdenada = (len(listaDePalabrasOrdenadasPorCantidadDeApariciones)*0.3)//1
        largoDeListaOrdenada = int(float(largoDeListaOrdenada))
        print("\nLas siguientes estadíticas son de las",largoDeListaOrdenada, "palabras más aparecidas en el texto.")

                    #En este if se calcula la cantidad de datos a mostrar en caso que sean menos de 10.#
    if(len(listaDePalabrasOrdenadasPorCantidadDeApariciones) <= 10):
        largoDeListaOrdenada = len(listaDePalabrasOrdenadasPorCantidadDeApariciones)
        print("\nLas siguientes estadíticas son de las",largoDeListaOrdenada, "palabras más aparecidas en el texto.")
    
    i=1
    while(i < largoDeListaOrdenada):
                                #Este print muestra las letras más utilizadas.#
        palabra = (listaDePalabrasOrdenadasPorCantidadDeApariciones[len(listaDePalabrasOrdenadasPorCantidadDeApariciones) -i]) 
        print("La probabilidad de esta palabra ->",palabra[1], "<- es: ",palabra[0]/(len(listaDePalabras)),"\n")
        i += 1


def generarTxt():
    ordenarPalabrasPorCantidadDeApariciones()
    archivo = open("archivoDePrueba.txt","w")
    archivo.write(f"{listaDePalabrasOrdenadasPorCantidadDeApariciones}",len(listaDePalabrasOrdenadasPorCantidadDeApariciones))
    archivo.close()




                                #Esta función se encarga de validar que que sea un número entero.#
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: \n"))
            correcto=True
        except ValueError:
            print('Porfavor introduce un numero entero\n')
     
    return num





                                    #Esta será la función principal, encargada organizar y brindar
                                    #lo que necesite el usuario.#
def menu():
    salir = False
    opcion = 0
 
    while not salir:
    
        print ("\n\n1. Consultar por una palabra.")
        print ("2. Consultar la probabilidad de las palabras más usadas.")
        print ("3. Generar txt.")
        print ("4. Salir\n")
        
        print ("Elige una opcion\n")
    
        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            consultarPalabra()
        elif opcion == 2:
            calcularProbabilidadDeLasMasAparecidas()
        elif opcion == 3:
            generarTxt()
        elif opcion == 4:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 4")
    
    print ("ADIOS")



extraerArchivosHtmDelDirectorio()
leerDocumentoHtm()
eliminarTildesAndMayusculas()
removerSignosDePuntuacion(textoSinMayusculasNiMinusculas,' ') #Reemplaza cada signo de puntuación por " "
removerNumeros()
separarPalabras()
menu()


#consultarPalabra()
#calcularProbabilidadDeLasMasAparecidas()