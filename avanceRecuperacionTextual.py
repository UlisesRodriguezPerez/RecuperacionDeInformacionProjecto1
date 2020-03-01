from bs4 import BeautifulSoup   #pip3 install bs4
from unicodedata import normalize
import requests                 #pip install requests
import urllib.request
import re
import string



SECCION1 = 0
SECCION2 = 1



                    #Todo el if se ejecuta cuando la SECCION1 esté activa.#
if(SECCION1 == 1):

                    #Variable en la que se obtendrá el html de la pagina.#
    variableParaHtml = requests.get('http://toscrape.com/', headers = {'Accept.Encoding': 'identy'})

                    #Imprime la variable con el html.#
    #print(variableParaHtml.content)

                    #Variable para parsear el codigo html( acomodandolo para utilizarlo más ordenado.)#
    soup = BeautifulSoup(variableParaHtml.content, 'html.parser')

                    #el .img nos da la primera etiqueta de imagen#
    #print(soup.img) 

                    #Para obtener la clase de la imagen.
                    #Lo que imprime es una lista con los objetos.#"
    #print(soup.img.get('class'))   

                    #Imprime el indice 0 de la lista. (logo)#
    #print(soup.img.get('class')[0]) 

                    #Imprime Una lista con todas las etiquetas que encuentre de img#
    #print(soup.find_all('img'))

                    #Con este for recorremos la lista e imprimimos 1x1. xD#
    #for imagen in soup.find_all('img'):
    #    print(imagen)

                    #Con este for imprimimos la ruta de cada imagen.#
    #for imagen in soup.find_all('img'):
    #    print("Ruta de la imagen: " + imagen.get('src'))

                    #Para obtener no solo las imagenes, sino tambíen todos los links (Etiquetas 'a')
                       #que nos ofrece la página.#
    #print(soup.find_all('a'))

                    #Obtenemos la misma información pero el link en si y en orden con el for#
    for link in soup.find_all('a'):
        print(link.get('href'))



                    #SECCION 2 
if(SECCION2 ==1):
    url = " file:///C:/Users/ulirp/Dropbox/Documentos%20TEC/III%20semestre/Recuperación%20de%20información%20textual/Proyectos/TP1/Geografia/América/Estados_soberanos/Costa_Rica.htm"

    req = urllib.request.urlopen(url)
    html = req.read()

                    #Se optiene el texto html#
    soup = BeautifulSoup(html) 

                    #Imprime el texto sin formato html.#
    #print(soup.get_text())

                    #Variable encargada de almacenar el texto#
    variableTexto = soup.get_text()
    #print(variableTexto)



                    #SECCION DONDE COMENZAREMOS A SEPARAR PALABRAS.#
## 
def leerTexto():
    global txt
    txt = variableTexto.lower()

                        #Una forma de quitar las tildes#
#    txt = re.sub(
#        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
#        normalize( "NFD", txt), 0, re.I
#    )
#    txt = normalize('NFC',txt)


                            #Otra forma de eliminar tíldes.#
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    txt = txt.translate(trans)

                                #Función para eliminar los signos de puntuación.#
def removerSignosDePuntuacion(txt, replace):
    global texto
    texto = re.sub('[%s]' % re.escape(string.punctuation), replace, txt)

                                #Función para separar palabras.#
def separarPalabras():
    global listaDePalabras
    global listaControlDePalabras
    listaDePalabras = []#La lista que contendrá todas las palabras.
    listaControlDePalabras = [] #Esta lista será la que contenga el registro o control de cada palabra.
    
                                        #Este for separará cada palabra y lo agregará a la lista.#
    for palabras in texto.split():  
        listaDePalabras.append(palabras)


                                        #Seccion para poder agrupar palabras y llevar un control de ellas.#

    for palabraPorCompara in range(len(listaDePalabras)):#Optiene la posicion de cada palabra para entonces proceder a 
                                                            #calcular cuando se repite.
        
        if(listaControlDePalabras):#En caso de la lista no estar vacía entonces continua con las demás instrucciones.
            bandera = 0 #Esta variable bandera se utilizará para distinguir cuando una palabra ya se ha repetido.
            
            for palabraYaCalculada in range(len(listaControlDePalabras)):#Este for se encargará de recorrer la lista (la cual comienza
                            #vacía) y en la cual se irán agregando las palabras que aún no se han repetido o que no se 
                            #encuentran aún en la lista.
                                                        

                                    #Este if se encarga de comparar la palabra de la lista de palabras totales, con
                                   #las palabras de la lista de palabras controladas (En la que no pueden haber repetidas)#
                if (listaDePalabras[palabraPorCompara] == listaControlDePalabras[palabraYaCalculada][1]):

                    listaControlDePalabras[palabraYaCalculada][0] += 1 #En caso de que ambas palabras sean iguales, unicamente se le 
                                       # sumará 1 al registro de esa palabra, porque significa que está repetida.#

                    bandera = 1 # Y se iguala la bandera a 1 para indicar que si se encontraba ya en el texto.
                    break
                                #Cuando la bandera sigue en 0 y no en 1, significa que la palabra no se encuentra aún en la lista 
                                #de palabras controladas, por lo tanto se procede con las demás intrucciones para agregarla a la lista.
            if(bandera == 0):
                listaControlDePalabras += [[1,listaDePalabras[palabraPorCompara]]] #Se agrega la palabra a la lista con un 
                                            #un registro inicial de 1 palabra.


                                        #Este else es unicamente para agregar la primer palabra, ya que la lista se encontraba
                                        #vacía.#                         
        else:
            listaControlDePalabras += [[1,listaDePalabras[palabraPorCompara]]]
    
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
           

    
    

    #print(listaDePalabrasOrdenadasPorCantidadDeApariciones)
    
def calcularProbabilidadDeLasMasAparecidas():

                    #Esta es la lista de palabras ordenadas según la cantidad de apariones.#
    global listaDePalabrasOrdenadasPorCantidadDeApariciones
    listaDePalabrasOrdenadasPorCantidadDeApariciones = sorted(listaControlDePalabras)

                    #En este if se calcula la cantidad de datos a mostrar en caso que sean más de 100.#
    if (len(listaDePalabrasOrdenadasPorCantidadDeApariciones) > 99):
        largoDeListaOrdenada = len(listaDePalabrasOrdenadasPorCantidadDeApariciones)*0.02
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
        print ("3. Próximante :D .")
        print ("4. Salir\n")
        
        print ("Elige una opcion\n")
    
        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            consultarPalabra()
        elif opcion == 2:
            calcularProbabilidadDeLasMasAparecidas()
        elif opcion == 3:
            print("\n***********Estamos trabajando en esta actualización.*********** \n***********Gracias por su paciencia :)***********")
        elif opcion == 4:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 4")
    
    print ("ADIOS")


leerTexto()
removerSignosDePuntuacion(txt,' ')   #Reemplaza cada signo de puntuación por " "
separarPalabras()
menu()
#consultarPalabra()
#calcularProbabilidadDeLasMasAparecidas()
                                            ####PENDIENTE QUITAR NÜMEROS, ¿ y " y verificar la Ñ/ñ