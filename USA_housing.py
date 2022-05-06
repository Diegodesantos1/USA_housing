import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("Housing.csv", sep= ",")
print(datos)
lista_Income = list(datos["Avg. Area Income"]) ; lista_Age = list(datos["Avg. Area House Age"]) ; lista_Rooms = list(datos["Avg. Area Number of Rooms"])
lista_Bedrooms = list(datos["Avg. Area Number of Bedrooms"]) ; lista_Population = list(datos["Area Population"]) ; lista_Price = list(datos["Price"]) ; lista_Address = list(datos["Address"])
class Analisis:
    def crear_diccionario():
        global diccionario
        diccionario = {}
        for i in range(len(datos)):
            diccionario[i] = datos.iloc[i]
        print(diccionario)
    def graficas_listaRooms():
        plt.subplot(1,2,1)
        plt.bar(lista_Rooms, lista_Income, color = "orange") ; plt.ylabel("Habitaciones") ; plt.xlabel("Sueldo")
        plt.subplot(1,2,2)
        plt.bar(lista_Rooms, lista_Age, color = "blue") ; plt.ylabel("Habitaciones") ; plt.xlabel("Edad de la casa")
        plt.show()
        plt.subplot(1,3,1)
        plt.bar(lista_Rooms, lista_Bedrooms, color = "red") ; plt.ylabel("Habitaciones") ; plt.xlabel("Casas")
        plt.subplot(1,3,2)
        plt.bar(lista_Rooms, lista_Population, color = "yellow") ; plt.ylabel("Habitaciones") ; plt.xlabel("Población")
        plt.subplot(1,3,3)
        plt.bar(lista_Rooms, lista_Price, color = "purple") ; plt.ylabel("Habitaciones") ; plt.xlabel("Precio")
        plt.show()
Analisis.crear_diccionario()
Analisis.graficas_listaRooms()
Analisis.graficas_listaPrice()