# Tarea semana 16 - Trabajo con Archivos de Texto
# Creamos un archivo llamado my_notes.txt
# Escribimos tres lineas de notas personales en el archivo

with open("my_notes.txt", "w") as Archivo_de_texto:

# Escribimos tres líneas de notas personales en el archivo
    Archivo_de_texto.write("Linea 1: Mi nombre es Liliana Maribel Bravo Caizaluisa y tengo 22 años\n")
    Archivo_de_texto.write("Linea 2: Vivo en la ciudad de Quito\n")
    Archivo_de_texto.write("Linea 3: Estudio en la Universidad Estatal Amazónica, en la carrera de Tecnologías de la Información\n")

# Cerramos el archivo de texto
    Archivo_de_texto.close()
    print("Archivo 'my_notes.txt' creado y escrito con éxito.")

# Abrimos el archivo "my_notes.txt" en modo lectura ("r")
    with open("my_notes.txt", "r") as Archivo_de_texto:
        Archivo_de_texto.seek(0)

# Procedemos a leer el contenido del archivo de texto línea por línea
        Linea_1 = Archivo_de_texto.readline()
        Linea_2 = Archivo_de_texto.readline()
        Linea_3 = Archivo_de_texto.readline()

# Cerramos el archivo de texto
        Archivo_de_texto.close()

# Mostramos el resultado de cada línea leída
        print("Contenido del Archivo")
        print(
            "1: ", Linea_1,
            "2: ", Linea_2,
            "3: ", Linea_3
        )

# Fin del programa
