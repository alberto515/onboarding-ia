from datetime import datetime

def imprimir_hola_mundo_y_fecha():
    print("Hola Mundo")
    print(datetime.now().strftime("%d-%m-%Y"))


if __name__ == "__main__":
    imprimir_hola_mundo_y_fecha()



# El prompt original no imprimía en el terminal el saludo y la fecha. Ha definido la función, pero le he especificado que imprima el saludo, 
# escribiéndolo entre comillas, y le he dado el formato necesario para la fecha. Además el import lo he puesto al principio del archivo.