import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("Housing.csv", sep= ",")
lista_Income = list(datos["Avg. Area Income"]) ; lista_Age = list(datos["Avg. Area House Age"]) ; lista_Rooms = list(datos["Avg. Area Number of Rooms"])
lista_Bedrooms = list(datos["Avg. Area Number of Bedrooms"]) ; lista_Population = list(datos["Area Population"]) ; lista_Price = list(datos["Price"]) ; lista_Address = list(datos["Address"])
