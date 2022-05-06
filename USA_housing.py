import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from introducir.numero import solicitar_introducir_numero_extremo

datos = pd.read_csv("USA_Housing.csv", sep= ",")
print(datos)
lista_Income = list(datos["Avg. Area Income"]) ; lista_Age = list(datos["Avg. Area House Age"]) ; lista_Rooms = list(datos["Avg. Area Number of Rooms"])
lista_Bedrooms = list(datos["Avg. Area Number of Bedrooms"]) ; lista_Population = list(datos["Area Population"]) ; lista_Price = list(datos["Price"]) ; lista_Address = list(datos["Address"])
class Analisis:
    def analisis_inicial():
        print("Las columnas del dataset son:")
        print(datos.columns)
        print("VARIABLES + DATOS")
        print(datos.head())
        print("La descripción del dataset es")
        print(datos.describe())
        print("La información del dataset es")
        print(datos.info())
    def crear_diccionario():
        global diccionario
        diccionario = {}
        for i in range(len(datos)):
            diccionario[i] = datos.iloc[i]
        print(diccionario)
    def graficas_listaRooms():
        plt.subplot(1,2,1)
        plt.bar(lista_Rooms, lista_Income, color = "red") ; plt.ylabel("Habitaciones") ; plt.xlabel("Sueldo")
        plt.subplot(1,2,2)
        plt.bar(lista_Rooms, lista_Age, color = "blue") ; plt.ylabel("Habitaciones") ; plt.xlabel("Edad de la casa")
        plt.show()
        plt.subplot(1,3,1)
        plt.bar(lista_Rooms, lista_Bedrooms, color = "green") ; plt.ylabel("Habitaciones") ; plt.xlabel("Casas")
        plt.subplot(1,3,2)
        plt.bar(lista_Rooms, lista_Population, color = "orange") ; plt.ylabel("Habitaciones") ; plt.xlabel("Población")
        plt.subplot(1,3,3)
        plt.bar(lista_Rooms, lista_Price, color = "purple") ; plt.ylabel("Habitaciones") ; plt.xlabel("Precio")
        plt.show()
    def histograma(variable):
        plt.figure(figsize = (9,3))
        plt.hist(datos[variable], bins = 50, color= "green")
        plt.xlabel(variable)
        plt.ylabel("Frecuencia")
        plt.title("Distribución variable {} con histograma".format(variable))
        plt.show()
    def calculos():
        print("="*50)
        mediaIncome = datos["Avg. Area Income"].mean() ; mediaAge = datos["Avg. Area House Age"].mean() ; mediaRooms = datos["Avg. Area Number of Rooms"].mean()
        mediaBedrooms = datos["Avg. Area Number of Bedrooms"].mean() ; mediaPopulation = datos["Area Population"].mean() ; mediaPrice = datos["Price"].mean()
        print("Media de la variable Income: ", mediaIncome,"\nMedia de la variable Age: ", mediaAge,"\nMedia de la variable Rooms : ", mediaRooms,"\nMedia de la variable Bedrooms: ", mediaBedrooms,"\nMedia de la variable Population: ", mediaPopulation,"\nMedia de la variable Precio: ", mediaPrice)
        print("="*50)
        varianzaIncome = datos["Avg. Area Income"].var() ; varianzaAge = datos["Avg. Area House Age"].var() ; varianzaRooms = datos["Avg. Area Number of Rooms"].var()
        varianzaBedrooms = datos["Avg. Area Number of Bedrooms"].var() ; varianzaPopulation = datos["Area Population"].var() ; varianzaPrice = datos["Price"].var()
        print("varianza de la variable Income: ", varianzaIncome,"\nvarianza de la variable Age: ", varianzaAge,"\nvarianza de la variable Rooms : ", varianzaRooms,"\nvarianza de la variable Bedrooms: ", varianzaBedrooms,"\nvarianza de la variable Population: ", varianzaPopulation,"\nvarianza de la variable Precio: ", varianzaPrice)
        print("="*50)
        desviacionIncome = datos["Avg. Area Income"].std() ; desviacionAge = datos["Avg. Area House Age"].std() ; desviacionRooms = datos["Avg. Area Number of Rooms"].std()
        desviacionBedrooms = datos["Avg. Area Number of Bedrooms"].std() ; desviacionPopulation = datos["Area Population"].std() ; desviacionPrice = datos["Price"].std()
        print("desviacion de la variable Income: ", desviacionIncome,"\ndesviacion de la variable Age: ", desviacionAge,"\ndesviacion de la variable Rooms : ", desviacionRooms,"\ndesviacion de la variable Bedrooms: ", desviacionBedrooms,"\ndesviacion de la variable Population: ", desviacionPopulation,"\ndesviacion de la variable Precio: ", desviacionPrice)

def iniciador ():
    eleccion=solicitar_introducir_numero_extremo("\n\n¿Qué desea hacer?\n1:Análisis inicial\n2: Diccionario con los datos\n3: Graficas de Barras\n4: Calculo de Media, Varianza y Desviación Típica\n5: Histogramas con todas las variables\n6: Finalizar\n\n", 1, 6)
    if eleccion == 1:
        Analisis.analisis_inicial()
        iniciador()
    elif eleccion == 2:
        Analisis.crear_diccionario()
        iniciador()
    elif eleccion == 3:
        Analisis.graficas_listaRooms()
        iniciador()
    elif eleccion == 4:
        Analisis.calculos()
        iniciador()
    elif eleccion == 5:
        variables = ["Avg. Area Income","Avg. Area House Age", "Avg. Area Number of Rooms", "Avg. Area Number of Bedrooms","Price", "Area Population"]
        for i in variables:
            Analisis.histograma(i)
        iniciador()
    elif eleccion == 6:
        exit()