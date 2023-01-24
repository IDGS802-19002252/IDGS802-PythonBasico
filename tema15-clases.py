import os


class OperasBas:
    # declaración de las propiedades

    # declaración de constructor
    def __init__(self):
        pass
    # declaración de métodos

    def suma(self, num1, num2):
        res = num1 + num2
        return res

    def resta(self, num1, num2):
        res = num1 - num2
        return res

    def multi(self, num1, num2):
        res = num1 * num2
        return res

    def div(self, num1, num2):
        res = num1 / num2
        return res


def main():
    ob = OperasBas()
    opt = -1
    res = 0
    while (opt != 0):
        opt = int(
            input('1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n0.- Salir'))
        if (opt == 0):
            break
        os.system('clear')
        num1 = int(input('Ingresa el primer número:'))
        num2 = int(input('Ingresa el segundo número:'))
        if (opt == 1):
            res = ob.suma(num1, num2)
        elif (opt == 2):
            res = ob.resta(num1, num2)
        elif (opt == 3):
            res = ob.multi(num1, num2)
        elif (opt == 4):
            res = ob.div(num1, num2)
        print('El resultado es: {}'.format(res))
        


if __name__ == "__main__":
    main()
