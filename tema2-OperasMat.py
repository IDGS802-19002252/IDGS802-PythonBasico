num1 = 20
num2 = 4
print('Suma ->', num1+num2)
print('Resta ->', num1-num2)
print('Mult ->', num1*num2)
print('Div ->', num1/num2)
print('Div exacta ->', num1//num2)
print('Potencia ->', num1**num2)

# concatenación ...

text1 = 'ola wenas'
text2 = 'tardes'
textF = text1 + ' ' + text2

print(textF)
print('Otra concatenación vea -> %s %s' %(text1, text2))

saludoProPlusMaxUltra = 'Otravez vea -> {} {}'.format(text1, text2)
print(saludoProPlusMaxUltra)

saludoProPlusMaxUltraPlus = 'Final orasi bro -> {x} {y}'.format(x=text1, y=text2)
print(saludoProPlusMaxUltraPlus)
