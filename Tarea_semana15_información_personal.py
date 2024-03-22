# Tarea semana15 Trabajando con Diccionarios
# Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona
# Debe incluir al menos las claves "nombre", "edad", "ciudad" y "profesion"

información_personal={
"Nombre": "Liliana Bravo",
"Edad": 22,
'Ciudad': "Quito"}

# Acceder al valor asociado con la clave "ciudad" y modifícarlo con una ciudad diferente
información_personal["Ciudad"] = "Santo Domingo"

# Agregamos una nueva clave-valor "Profesion"
información_personal["Profesión"] = "Estudiante de Tecnologías de la Información"

# Agregamos la clave "Teléfono"
información_personal["Teléfono"] = "0985086408"   # se agregó un número de teléfono ficticio

# Eliminamos la clave "Edad"
información_personal ["Edad"]

# Imprimimos el diccionario resultante después de realizar todas las operaciones
print(información_personal)