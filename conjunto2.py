frutas = {"Maçã", "banana", "uva", "laranja"}
frutas2 = {"pessego", "banana", "tangerina"}

resultado = frutas.intersection(frutas2)

if resultado:
    print(f"A fruta {frutas2} está presente")
else:
    print(f"A fruta {frutas2} não está no conjunto")