print ("---BIENVENID@---")
print ()
menu_panaderia = {
    "Panadería": {
        "Productos": {
            "Pan blanco": 2000,
            "Pan integral": 3000,
            "Croissant": 1800,
            "Bollos de canela": 2200,
            "Palmera de chocolate": 1500,
            "Rosquillas": 1000,
            "Baguette": 2800,
            "Pan de centeno": 3500,
            "Panecillos de leche": 1200,
            "Eclairs": 2000,
            "Promoción del dia compra 2 panes blancos y el tercero llevatelo a mitad de precio": 5000
        },
        
    },
    "Pasteles": {
        "Productos": {
            "Tarta de manzana": 15000,
            "Tarta de fresa": 14500,
            "Pastel de chocolate": 18000,
            "Cheesecake": 16500,
            "Tarta de zanahoria": 17500,
            "Cupcakes": 2000,
            "Galletas decoradas": 1500,
            "Rollitos de canela": 2500,
            "Brownies": 2500,
            "Magdalenas": 1200,
            "Promoción de Sabatina paga 1 cupcake y lleva 2": 2000
        },
        
    },
    "Bebidas": {
        "Productos": {
            "Café": 1500,
            "Té": 2000,
            "Zumo de naranja": 2000,
            "Batido de frutas": 3000,
            "Refresco": 1800,
            "Agua mineral": 1000,
            "Cerveza artesanal": 3500,
            "Café con leche": 2000,
            "Chocolate caliente": 2500,
            "Limonada": 2200,
            "Promoción de fin de semana batido de frutas a mitad de precio" : 1500
        },
        
    }
}

print("ESTE ES NUESTRO MENÚ:")
print ()
for categoria, datos_categoria in menu_panaderia.items():
    print(f"--- {categoria} ---")
    for i, (producto, precio) in enumerate(datos_categoria["Productos"].items(), 1):
        print(f"{i}. {producto}: ${precio}")
    print()

print("Afortunadamente contamos con 3 excelentes categorías en las que puedas elegir tu plato o bebida prefererida: ")
print ()

opcionCategoria = list(menu_panaderia.keys())  
for i, val in enumerate(opcionCategoria, 1): 
    print(f"{i}. {val}")
print ()

datosCategoria = (input("Por favor, selecciona el número de la categoría del producto en la que estás interesad@ => "))
if datosCategoria.isdigit():
    datosCategoria = int(datosCategoria)
else:
    print("Entrada inválida. Por favor, ingresa un número válido.")
print ()

if 1 <= datosCategoria <= len(opcionCategoria):
    categoria_seleccionada = opcionCategoria[datosCategoria - 1]
    productosCategoriaSeleccionada = menu_panaderia[categoria_seleccionada]["Productos"]
    for i, (producto, precio) in enumerate(productosCategoriaSeleccionada.items(), 1):  
        print(f"{i}. {producto}: ${precio}")
    print ()

    producto_seleccionado = int(input("Por favor, selecciona el número asignado al producto o la promoción en la que estás interesad@ => "))
    print ()

    if 1 <= producto_seleccionado <= len(productosCategoriaSeleccionada):
        producto_seleccionado = list(productosCategoriaSeleccionada.keys())[producto_seleccionado - 1]
        precio_producto = productosCategoriaSeleccionada.get(producto_seleccionado)

        if producto_seleccionado.startswith("Promoción"):
            print(f"Has seleccionado la promoción: {producto_seleccionado}. Debes pagar ${precio}")
            cantidad_pagada = int(input("Por favor, ingresa la cantidad con la que pagarás => "))
            if cantidad_pagada < precio:
                    print("La cantidad ingresada es insuficiente. Por favor, ingresa una cantidad válida.")
            else:
                    vuelto = cantidad_pagada - precio
                    print(f"Gracias por tu compra. Tu vuelto es de ${vuelto}")
        else:
            print("Has seleccionado el producto:", producto_seleccionado)
            productos_seleccionados = int(input("Por favor, selecciona la cantidad que deseas comprar => "))
            print()

            if 1 <= productos_seleccionados:
                total = precio_producto * productos_seleccionados
                print(f"Total a pagar por {productos_seleccionados} {producto_seleccionado}: ${total}")
                cantidad_pagada = float(input("Por favor, ingresa la cantidad con la que pagarás => "))
                if cantidad_pagada < total:
                    print("La cantidad ingresada es insuficiente. Por favor, ingresa una cantidad válida.")
                else:
                    vuelto = cantidad_pagada - total
                    print(f"Gracias por tu compra. Tu vuelto es de ${vuelto}")
            else:
                print("Opción no válida. Por favor, selecciona un número de producto válido.")
    else:
        print("Opción no válida. Por favor, selecciona un número de producto o promoción válido.")
else:
    print("Opción no válida. Por favor, selecciona un número de categoría válido.")


     



