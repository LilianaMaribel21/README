# Tarea semana 14 Calculo de descuento en compras
# Crear una función que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento.
# La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
# La función debe devolver el monto del descuento calculado.

def calcular_descuento(monto_total, porcentaje_descuento= 25):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Proporcionamos el monto total de la compra
monto_compra_1 = 650
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

print("Para una compra de $", monto_compra_1, "el descuento es de $", descuento_1, "(", 'porcentaje_descuento_1', "%) y el monto final a pagar es de $", monto_final_1)

# Proporcionamos el monto total de la compra y el porcentaje de descuento
monto_compra_2 = 280
porcentaje_descuento_2 = 55
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

print("Para una compra de $", monto_compra_2, "con un descuento del $", porcentaje_descuento_2, "%, el descuento es de $", descuento_2, "(", porcentaje_descuento_2, "%) y el monto final a pagar es de $", monto_final_2)

#Fin del caáculo de descuento en las compras