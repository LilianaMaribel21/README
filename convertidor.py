# Crear una función para convertir grados centigrados a grados Fahrenheit, a grados Kelvin
# Fahrenheit = (9/5)*(grad_cent)+32
# Kelvin = 273.15+grad_cent

def conversor(grados_cent):
    Fahrenheit = (9 / 5) * (grados_cent) + 32  # transdormamos grados centigrados a Fahrenheit
    Kelvin = 273.15+grados_cent  # transformamos grados centigrados a Kelvin

    return Fahrenheit, Kelvin

centigrados=int(input("ingresar datos centigrados="))

result_fahrenheit, result_kelvin = conversor(centigrados)

print(centigrados, "grados centrigrados es igual a", result_fahrenheit, "grados Fahrenheit")
print(centigrados, "grados centigrados es igual a", result_kelvin, "grados Kelvin")
