# Prueba Recuperativa Unidad 1 / Matías Fonseca / Programación 1 2021
import json


def carga_archivo_json(archivo=None):
    """Carga del archivo JSON"""

    try:
        with open("iris.json", "r") as archivo_json:
            datos = json.load(archivo_json)
            return datos
    except FileNotFoundError:
        print("Error, el archivo no fue encontrado")
        quit()

# Función que muestra los nombres de las especies.
def nombre_especies(datos):

    especie = None

    for item in datos:
        if especie != item['species']:
            print('Especie :', item['species'])
            especie = item['species']

# Función que saca el promedio del ancho de las especies.
def promedio_ancho_largo(datos, especies, tipo):
    
    promedio = 0 
    contador = 0

    for item in datos:

        if tipo == "ancho":
            if  item['species'] == especies:
                promedio = item['petalWidth'] + promedio
                contador = contador + 1

            elif item['species'] != especies and contador != 0:
                resultado = promedio / contador                    
                return resultado

            if item['species'] == 'virginica' and contador == 50:
                resultado = promedio / contador                    
                return resultado

        if tipo == "largo":
            if  item['species'] == especies:
                promedio = item['petalLength'] + promedio
                contador = contador + 1

            elif item['species'] != especies and contador != 0:
                resultado = promedio / contador                    
                return resultado

            if item['species'] == 'virginica' and contador == 50:
                resultado = promedio / contador                    
                return resultado

        if tipo == "especie":
            if  item['species'] == especies:
                contador = contador + 1

            elif item['species'] != especies and contador != 0:
                print("El rango de las", especies, "es de", contador - 3, "y", contador + 3 )
                return 
                
            if item['species'] == 'virginica' and contador == 50:
                print("El rango de las", especies, "es de", contador - 3, "y", contador + 3 )

# Función para saber la medida máxima del sepalo y a que especie corresponde.
def max_sepal(datos):

    maximo_sepal = 0
    especie = None

    for item in datos:
        if maximo_sepal < item['sepalLength']:
            maximo_sepal = item['sepalLength']
            especie = item['species']

    print("La medida máxima para el alto de un sépalo es de", maximo_sepal, "y corresponde a la especie", especie)

# Función que crea los nuevos archivos JSON.
def nuevos_json(datos):

    l1 = []
    l2 = []
    l3 = []

    for item in datos:
        if item['species'] == 'setosa':
           l1.append(item)

        if item['species'] == 'versicolor':
           l2.append(item)

        if item['species'] == 'virginica':
           l3.append(item)        
    
    #setosa_json = json.dumps(l1, indent="")
    #print(setosa_json)
    with open('setosa.json', 'a') as archivo:
        json.dump(l1, archivo, indent=4)

    with open('versicolor.json', 'a') as archivo:
        json.dump(l2, archivo, indent=4) 

    with open('virginica.json', 'a') as archivo:
        json.dump(l3, archivo, indent=4)    

# Función que hace de menú principal para este programa.
def menu():

    archivo = 'iris.json'
    datos = carga_archivo_json(archivo)
    choice = -1

    print("                                  Menu principal de base de datos                                        ")
    print("¿Qué desea consultar? Ingrese el dígito de la opción que desee: ")
    print("1: Nombre de las especies existentes.")
    print("2: Promedio ancho y alto de los pétalos por especie.")
    print("3: ¿Qué especie tiene en promedio los pétalos más anchos y más altos?")
    print("4: Promedio de cada especie, en un rango -3 y +3.")
    print("5: ¿Cuál es la medida máxima para el alto de un sépalo y a que especie le corresponde?.")
    print("6: Creación de nuevos archivos.")
    print("Pulse '0' para salir de la base de datos")
    print(" ")

    try:
        choice = int(input())
        print(" ")
    except ValueError:
        print("Ingrese un dígito por favor.")

    if choice == 0:
        print("Gracias por utilizar la base de datos.")
        print("Nos vemos en otra ocasión, que tenga un buen día.")
        quit()

    elif choice == 1:
        print("Los nombres de las especies existentes son:")
        nombre_especies(datos)
        print(" ")

        menu()

    elif choice == 2:
        print("El promedio de ancho y largo de la setosa es: ")
        print("Ancho: ", promedio_ancho_largo(datos, "setosa", "ancho"))
        print("Largo: ", promedio_ancho_largo(datos, "setosa", "largo"))
        print(" ")

        print("El promedio de ancho y largo del versicolor es: ")
        print("Ancho: ", promedio_ancho_largo(datos, "versicolor", "ancho"))
        print("Largo: ", promedio_ancho_largo(datos, "versicolor", "largo"))
        print(" ")

        print("El promedio de ancho y largo de la virginica es: ")
        print("Ancho: ", promedio_ancho_largo(datos, "virginica", "ancho"))
        print("Largo: ", promedio_ancho_largo(datos, "virginica", "largo"))
        print(" ")

        menu()

    elif choice == 3:
        print("Según los resultados obtenidos en el cálculo del promedio de las 3 especies.")
        print("La especie que en promedio tiene los pétalos más anchos y largos es la virginica.")
        print("Con un valor de", promedio_ancho_largo(datos, "virginica", "ancho"), "en el ancho ")
        print("Y con un valor de", promedio_ancho_largo(datos, "virginica", "largo"), "en el largo.")
        print(" ")

        menu()

    elif choice == 4:
        promedio_ancho_largo(datos, "setosa", "especie")
        print(" ")

        promedio_ancho_largo(datos, "versicolor", "especie")
        print(" ")

        promedio_ancho_largo(datos, "virginica", "especie")
        print(" ")

        menu()

    elif choice == 5:
        max_sepal(datos)
        print(" ")

        menu()

    elif choice == 6:
        nuevos_json(datos)
        print("Se crearon los nuevos archivos, gracias por la espera.")
        print(" ")

        menu()

    else:
        print("Ingrese un dígito disponible.")
        print(" ")

        menu()

if __name__ == "__main__":
    #Llamado de la función menu.
    menu()