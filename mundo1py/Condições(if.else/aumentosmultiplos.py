salario = float(input('Qual seu salário? R$'))
if salario <= 1.250:
    novo = salario + (salario * 10 / 100)
    print('Seu salário com aumento de 10% fica R${:.2f}'.format(novo))
else:
    novo1 = salario + (salario * 15 / 100)
    print('Seu salário com aumento de 15% fica R${:.2f}'.format(novo1))
