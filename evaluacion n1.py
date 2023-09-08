from tabulate import tabulate



# Precio de las mascarillas

precio_mascarilla = 1000

precio_mascarilla_diseño = 1300



# Solicitar al cliente la cantidad de mascarillas que desea comprar

cantidad_mascarillas = int(input("Ingrese la cantidad de mascarillas simples que desea comprar: "))

cantidad_mascarilla_diseño = int(input("\nIngrese la cantidad de mascarillas con diseño que desea comprar: "))




# Calcular el costo total de las mascarillas

subtotal_simple = precio_mascarilla * cantidad_mascarillas

subtotal_diseño = precio_mascarilla_diseño * cantidad_mascarilla_diseño



# Solicitar al cliente la información de envío y calcular el costo de envío

comuna = input("\nIngrese su comuna-local-lejana: ").lower()

envio_gratis = subtotal_simple + subtotal_diseño > 15000

envio_costo = 0



if not envio_gratis:

  if comuna == "local":

    envio_costo = 1000

  elif comuna == "lejana":

    envio_costo = 3000



# Calcular el total a pagar

total = subtotal_simple + subtotal_diseño + envio_costo



# Crear una lista con los datos de la tabla

data = [

  ["Producto", "Cantidad", "Precio"],

  ["Mascarillas simples", cantidad_mascarillas, f"${precio_mascarilla}"],

  ["Mascarillas con diseño", cantidad_mascarilla_diseño, f"${precio_mascarilla_diseño}"],

  ["Costo de envío", comuna, f"${envio_costo}"],

  ["Costo total de las mascarillas", "", f"${subtotal_simple + subtotal_diseño}"],

  ["Total a pagar", "", f"${total}"]

]



# Crear la tabla utilizando tabulate

tabla_resumen = tabulate(data, headers="firstrow", tablefmt="pretty")



# Imprimir la tabla de resumen de compra

print("\nResumen de la compra:")

print(tabla_resumen)
 #Alex Sanhueza, Matias Toro, Benjamin Valenzuela