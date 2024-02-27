menu_panaderia = {
    "Panadería": {
        "Productos": {
            "Pan blanco": 2500,
            "Pan integral": 3000,
            "Croissant": 1800,
            "Bollos de canela": 2200,
            "Palmera de chocolate": 1500,
            "Rosquillas": 1000,
            "Baguette": 2800,
            "Pan de centeno": 3500,
            "Panecillos de leche": 1200,
            "Eclairs": 2000
        },
        "Promoción": "¡Compra 3 panes y llévate una rosquilla gratis!"
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
            "Magdalenas": 1200
        },
        "Promoción": "¡Paga 1 cupcake y lleva 2!"
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
            "Limonada": 2200
        },
        "Promoción": "¡Batido de frutas a mitad de precio!"
    }
}

print("Bienvenido a la panadería. Este es nuestro menú:")
for categoria, datos_categoria in menu_panaderia.items():
    print(f"--- {categoria} ---")
    for i, (producto, precio) in enumerate(datos_categoria["Productos"].items(), 1):
        print(f"{i}. {producto}: ${precio}")
    print(f"Promoción: {datos_categoria['Promoción']}")
    print()

print("¿Que categoría te interesa?")
listCategoria = list(menu_panaderia.keys())
for i,val in enumerate(listCategoria):
    print(f"{i+1}. {val}")
opcionCategoria = int(input("Por favor, selecciona la categoria en la que estas intersad@ => "))-1
datosCategoria = menu_panaderia.get(listCategoria[opcionCategoria])
productosCategoria = datos_categoria["Productos"]
print()

print("Ok, ahora es momento de elegir el producto")
opcionCategoria = list(productosCategoria.keys())
for i,val in enumerate(opcionCategoria):
    print(f"{i+1}. {val}")
datosCategoria = int(input("Por favor, selecciona el producto en el que estas intersad@ => "))-1

