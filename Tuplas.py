productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))
print ("Menú de selección de productos")

for i,val in enumerate(productos):
    print (f""" {i+1}. {val} ${precios[i]} """)

opción = int(input("Selecciona un producto => "))-1

print(f"Usuario seleccionaste el {productos[opción]} con un valor de ${precios[i]}")
dinero = int(input("Ingrese la cantidad de dinero disponible => "))
vueltos = dinero - precios [opción] 
if dinero >= precios [opción]:
    print(f"Compraste {productos[opción]} con un valro de ${precios[opción]}, sus vuletos son ${vueltos}")
else:
    print(f"El producto que desea comprar {productos[opción]} tiene un valor de ${precios[opción]}, le falta un total de ${- vueltos}")

