import requests
import json
import statistics

url="https://restcountries.com/v3.1/region/america?fields=name,area,unMember,languages,independent,population"

respuesta = requests.get(url)
lista_datos=[]

if respuesta.status_code==200:
	datos=respuesta.json()
	with open('datos.json', 'w') as archivo:
		json.dump(datos, archivo, indent=4)

	for pais in datos:
		if pais.get("independent")==True:
			nombre=pais["name"]["common"]
			area=pais["area"]
			lenguajes=list(pais["languages"].values())
			miembro_onu=pais["unMember"]
			poblacion=pais["population"]

			lista_datos.append({"País":nombre, "Área": area, "Lenguajes": lenguajes, "Población": poblacion, "Miembro de la Onu": miembro_onu,})
	


datos_america=str(lista_datos)

with open('paises_america.txt', 'a') as archivo:
	archivo.write(datos_america)


def main_areas(lista_datos):
	areas=[]
	for i in range (len(lista_datos)):
		a=lista_datos[i]["Área"]
		areas.append(a)
	return areas
main_areas(lista_datos)

def analisis_areas(areas):
	print(f"El area promedio de los países en Ámerica es: {statistics.mean(areas):.2f} kilometros cuadrados")
	print(f"Mediana: {statistics.median(areas):.2f} kilometros cuadrados")
areas=main_areas(lista_datos)
analisis_areas(areas)






