<h1 align="center">USA Housing</h1>

---
En este [repositorio](https://github.com/Diegodesantos1/USA_housing) queda resuelto el ejercicio del datset de USA Housing. Para llevar a cabo el proyecto me he documentado a través de la teoría que se encuentra en el campus virtual y otras fuentes.
***

El código empleado para resolverlo es el siguiente: 

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from introducir.numero import solicitar_introducir_numero_extremo

datos = pd.read_csv("USA_Housing.csv", sep= ",")
datos.fillna(0, inplace=True)
print(datos)
lista_Income = list(datos["Avg. Area Income"]) ; lista_Age = list(datos["Avg. Area House Age"]) ; lista_Rooms = list(datos["Avg. Area Number of Rooms"])
lista_Bedrooms = list(datos["Avg. Area Number of Bedrooms"]) ; lista_Population = list(datos["Area Population"]) ; lista_Price = list(datos["Price"]) ; lista_Address = list(datos["Address"])
class Analisis:
    def analisis_inicial():
        print("Las columnas del dataset son:")
        print(datos.columns)
        print("Las variables con los datos")
        print(datos.head())
        print("La descripción del dataset es")
        print(datos.describe())
    def crear_diccionario():
        global diccionario
        diccionario = {}
        for i in range(len(datos)):
            diccionario[i] = datos.iloc[i]
        print(diccionario)
    def barras(variable):
        plt.figure(figsize = (9,4)) ; plt.bar(lista_Rooms, datos[variable] , color= "green")
        plt.xlabel("Habitaciones") ; plt.ylabel(variable)
        plt.title("Gráfico de barras de {}".format(variable))
        plt.savefig(f"img/Barras/{variable}.png")
        plt.show()
    def histograma(variable):
        plt.figure(figsize = (9,4)) ; plt.hist(datos[variable], bins = 50, color= "green")
        plt.xlabel(variable) ;plt.ylabel("Frecuencia")
        plt.title("Distribución variable {} con histograma".format(variable))
        plt.savefig(f"img/Histogramas/{variable}.png")
        plt.show()
    def calculos():
        global mediaIncome, mediaAge, mediaRooms, mediaBedrooms, mediaPopulation, mediaPrice
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
        print("Desviacion de la variable Income: ", desviacionIncome,"\nDesviacion de la variable Age: ", desviacionAge,"\nDesviacion de la variable Rooms : ", desviacionRooms,"\nDesviacion de la variable Bedrooms: ", desviacionBedrooms,"\nDesviacion de la variable Population: ", desviacionPopulation,"\nDesviacion de la variable Precio: ", desviacionPrice)
    def maximo_minimos(variable):
        maxim = max(datos[variable]) ; minim = min(datos[variable])
        print (f"\nEl máximo de {variable} es {maxim}")
        print (f"\nEl mínimo de {variable} es {minim}")

def iniciador ():
    eleccion=solicitar_introducir_numero_extremo("\n\n¿Qué desea hacer?\n1: Análisis inicial\n2: Diccionario con los datos\n3: Graficas de Barras\n4: Calculo de Media, Varianza y Desviación Típica\n5: Histogramas\n6: Máximos y mínimos\n7: Finalizar\n", 1, 6)
    if eleccion == 1:
        Analisis.analisis_inicial()
        iniciador()
    elif eleccion == 2:
        Analisis.crear_diccionario()
        iniciador()
    elif eleccion == 3:
        variables = ["Avg. Area Income","Avg. Area House Age", "Avg. Area Number of Rooms", "Avg. Area Number of Bedrooms","Price", "Area Population"]
        for i in variables:
            Analisis.barras(i)
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
        variables = ["Avg. Area Income","Avg. Area House Age", "Avg. Area Number of Rooms", "Avg. Area Number of Bedrooms","Price", "Area Population"]
        for i in variables:
            Analisis.maximo_minimos(i)
        iniciador()
    elif eleccion == 7:
        exit()
```

Las imágenes de los gráficos de barras son:

![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Barras/Area%20Population.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Barras/Avg.%20Area%20House%20Age.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Barras/Avg.%20Area%20Income.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Barras/Avg.%20Area%20Number%20of%20Bedrooms.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Barras/Avg.%20Area%20Number%20of%20Rooms.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Barras/Price.png)

Las imágenes de los histogramas son:

![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Histogramas/Area%20Population.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Histogramas/Avg.%20Area%20House%20Age.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Histogramas/Avg.%20Area%20Income.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Histogramas/Avg.%20Area%20Number%20of%20Bedrooms.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Histogramas/Avg.%20Area%20Number%20of%20Rooms.png)
![Image text](https://github.com/Diegodesantos1/USA_housing/blob/main/img/Histogramas/Price.png)
