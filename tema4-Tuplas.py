# Tuplas no son inmutables

tupla1 = ('uno', 'dos', 'tres', 4, [0, 1, 2], True, 1.1)
tupla2 = ('uno', 'dos', 'tres')

tuplaMasTupla = (1,2,3,4, tupla1, 'ola')

print(tuplaMasTupla)

print(tuplaMasTupla[1])
print(tuplaMasTupla[-1])
print(tupla1[:2])

# destructuring
a,b,c = tupla2

print(a)
print(b)
print(c)

