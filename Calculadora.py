# coletando os valores para realização do calculo

num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número:'))
tipoOperacao = input('Digite o tipo de operação (+, -, *, /):')
# realizando os calculos de acordo com as informações fornecidas na etapa anterior
if tipoOperacao == '+':
    print('A soma é:', num1 + num2)
elif tipoOperacao == '-':
    print('A subtração é:', num1 - num2)
elif tipoOperacao == '*':
    print('A multiplicação é:', num1 * num2)
elif tipoOperacao == '/':
    print('A divisão é:', num1 / num2)
else:
    print('Operação inválida')