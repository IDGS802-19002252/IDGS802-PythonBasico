'''
Listas.
Una lista es una secuencia de elementos.
Cuando se asigna a una variable, permite agregar varios elementos
en un solo lugar.
Se crean con los corchetes o con la keyword list.
'''

lista1 = ['Juan', 23, 9.5, True, 'Chio', 500, 10]
print(lista1)
print(lista1[2])
print(lista1[-1])
print(lista1[:3])
print(lista1[3:])
lista1.append('ola wenas')
print(lista1)
lista1.insert(1, 'Felipino')
print(lista1)
lista1.extend(['cuatro', 2.1, False])
print(lista1)
lista1.remove(23)
print(lista1)
lista1.pop()
print(lista1)
lista2 = ['diez', 'once']
sumaListas = lista1 + lista2
print(sumaListas)
print(lista1*3)

lista3 = [1, 22, 4, 33, 4, 54, 5, 34, 32, 4, 5]
lista3.sort()
print(lista3)
