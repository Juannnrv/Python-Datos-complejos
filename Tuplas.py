productos = tuple(("Coca cola", "Pepsi cola"))
productos = list(productos)
productos.insert(1, "Manzana") #insert = Agregar un elemento en una posición determinada (posición, "elemento")
productos.append("Colombiana") #append = Agregar un elemento al final de la lista
productos.count("Pepsi cola") #count = Contar cantidad de apariciones elementos
productos.index("Manzana") #index = Obtener número de índice o posición
productos = tuple(productos)
print (productos)

