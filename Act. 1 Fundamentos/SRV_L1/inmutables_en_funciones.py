def agregar_elemento(lista):
    lista.append(4)

numeros = [1, 2, 3]
print(numeros)
print(id(numeros))


agregar_elemento(numeros)
print(numeros)  # [1, 2, 3, 4] (sí cambió)
print(id(numeros))