import requests
import json
import pandas as pd
 
def obtener_datos():
	url="https://restcountries.com/v3.1/region/america?fields=name,area,unMember,languages,independent,population,translations,capital"
	lista_datos=[]
	try:
		respuesta = requests.get(url, timeout=10)
		if respuesta.status_code==200:
			datos_paises=respuesta.json()
			with open('datos_paises.json', 'w') as archivo:
				json.dump(datos_paises, archivo, indent=4)
			for pais in datos_paises:
				if pais.get("independent")==True:
					nombre=pais["translations"]["spa"]["common"]
					area=pais["area"]
					lenguajes=list(pais["languages"].values())
					capital=pais["capital"]
					poblacion=pais["population"]
					lista_datos.append({"País":nombre, "Área": area, "Lenguajes": lenguajes, "Población": poblacion, "Capital": capital})
	
			with open('paises_america.json', 'w') as archivo:
				json.dump(lista_datos, archivo, indent=4)
	except:
		print("Error de conexión. Buscando datos locales...")
	finally:
		if not lista_datos:
			try:
				with open('paises_america.json', 'r') as archivo:
					lista_datos=json.load(archivo)
			except FileNotFoundError:
				print("El archivo no fue encontrado")
			except IOError:
				print("Error al acceder al archivo")	
	
	return(lista_datos)

def excel(lista_datos):
	df=pd.DataFrame(lista_datos)
	archivo_ruta='datos_america.xlsx'
	df.to_excel(archivo_ruta, index=False)
	print("Archivo de excel creado exitosamente")




