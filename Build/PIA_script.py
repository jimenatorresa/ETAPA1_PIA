import PIA_modulo
import PIA_modulo
lista_datos = PIA_modulo.obtener_datos()

opcion=""
while opcion!="13":
	print("Menú")
	print("1.Datos de un país especifico de Ámerica")
	print("2.Mediana y media de las áreas")
	print("3.Gráfico de línea país-área")
	print("4.País con menor población")	
	print("5.Gráfica barras de los 5 países con menor población")
	print("6.País con mayor población")
	print("7.Gráfica barras de los 5 países con mayor población")
	print("8.Frecuencia de idiomas en Ámerica")
	print("9.Gráfica de barras frecuencia de idiomas en Ámerica")
	print("10.Porcentaje de idiomas")
	print("11.Gráfica de pastel porcentaje de idiomas")
	print("12.Crear un archivo de excel con todos los datos")
	print("13.Salir")

	opcion=input("Elija un número:")
