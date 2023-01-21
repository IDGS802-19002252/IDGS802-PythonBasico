num1 = 20
num2 = 0

# print('la división de {0} entre {1} es de {2}'.format(num1, num2, (num1/num2)))

try:
    res = num1 / num2
except ZeroDivisionError:
    print('No jaló bro')
finally:
  print('Bai')
