if num1 > num2:
  print('el {} es mayor que {}'.format(num1,num2))
else:
  print('el {1} es mayor que {0}'.format(num1,num2))


# edad 

edad = int(input('ingresa la edad:'))

if edad > 18:
  print('eres mayor de edad')
elif edad == 18:
  print('Tienes 18')
else:
  print('No eres mayor de edad')