#Cálculo de Descuento en Compras
# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal

# Factura con dos productos
producto_1 = 150  # Precio del Producto 1
producto_2 = 200  # Precio del Producto 2

# Monto total de la compra
monto_total = producto_1 + producto_2

# Llamada 1: Solo monto total y porcentaje por defecto (10%)
descuento1 = calcular_descuento(monto_total)
monto_final1 = monto_total - descuento1

# Llamada 2: Monto total y un porcentaje de descuento personalizado (20%)
descuento2 = calcular_descuento(monto_total, 20)
monto_final2 = monto_total - descuento2

# Mostrar los resultados como si fuera una factura

print("Factura de Compra:")
print(f"Producto 1: ${producto_1}")
print(f"Producto 2: ${producto_2}")
print(f"Total sin descuento: ${monto_total}")

print("\nLlamada 1: Descuento del 10%")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto a pagar después del descuento: ${monto_final1}\n")

print("Llamada 2: Descuento del 20%")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto a pagar después del descuento: ${monto_final2}")

#Resultado:
#Factura de Compra:
#Producto 1: $150
#Producto 2: $200
#Total sin descuento: $350

#Llamada 1: Descuento del 10%
#Descuento aplicado: $35.0
#Monto a pagar después del descuento: $315.0

#Llamada 2: Descuento del 20%
#Descuento aplicado: $70.0
#Monto a pagar después del descuento: $280.0