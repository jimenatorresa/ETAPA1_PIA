import requests
import json
import statistics
def obtener_datos():
	url="https://restcountries.com/v3.1/region/america?fields=name,area,unMember,languages,independent,population,translations"
	respuesta = requests.get(url)
	lista_datos=[]
	if respuesta.status_code==200:
		datos_paises=respuesta.json()
		with open('datos_paises.json', 'w') as archivo:
			json.dump(datos_paises, archivo, indent=4)
		for pais in datos_paises:
			if pais.get("independent")==True:
				nombre=pais["translations"]["spa"]["common"]
				area=pais["area"]
				lenguajes=list(pais["languages"].values())
				miembro_onu=pais["unMember"]
				poblacion=pais["population"]
				lista_datos.append({"País":nombre, "Área": area, "Lenguajes": lenguajes, "Población": poblacion, "Miembro de la Onu": miembro_onu,})
		datos_america=str(lista_datos)
		with open('paises_america.txt', 'w') as archivo:
			archivo.write(datos_america)
		return lista_datos 






