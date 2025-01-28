precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, 'ciruela': 2.45, 'durazno': 4.55, 'melon': 7.35, 'sandia': 9.70, 'anana': 11.25}

compra = [(2, "manzana"), (2.5, "banana"), (1, "kiwi"), (3,"pera"),(1,"ciruela"),(2,"durazno"), (5,"melon"),(10,"sandia"),(3, "anana")]

total = 0

for cantidad, producto in compra:
    if producto in precios:
        total += cantidad * precios[producto]

print ("El total de la compra fue $", total)
