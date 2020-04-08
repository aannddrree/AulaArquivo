#EXEMPLO UTILIZANDO DEFs

def somar(a,b):
    return a + b

def imprimir(operacao):
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))

    if (operacao == '+'):
        r = somar(a,b)
    if (operacao == '-'):
        r = a - b
    return r

def main():
    try:
        print("O resultado é: " + str(imprimir('-')))
    except:
        print('Erro ao receber os dados')

main()
