def guardar_pedido(nombre, apellidos):

    with open("pedidos.txt", "w", encoding="utf-8") as file:
      file.write(nombre + " " + apellidos + "\n")
      file.close()