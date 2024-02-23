# Projeto calculadora.
# 23/02/2024

while True:
    while True:
        operacao = str(input('Digite o cálculo que deseja fazer [X PARA SAIR]: ')).replace(' ', '')
        if operacao.lower() == 'x':  # button to stop the program
            break
        elif operacao == '':  # blank space
            print()
            continue

        # - Filters the input in order to make the use of the expression 'eval' more secure
        # - (the eval expression could represent a security flaw in the code if not filtered)
        else:
            x = ''
            calculo = list(operacao)
            for elemento in calculo:
                if elemento.isdigit():
                    pass
                elif elemento == '+':
                    pass
                elif elemento == '-':
                    pass
                elif elemento == '*':
                    pass
                elif elemento == '/':
                    pass
                elif elemento == '(':
                    pass
                elif elemento == ')':
                    pass
                else:
                    x = 'ERROR'
            if x == 'ERROR':
                print('APENAS NÚMEROS E SÍMBOLOS MATEMÁTICOS [ + - * / ]')
                print()
            else:
                break
        #-----------------------------------------------------------------

    if operacao.lower() == 'x':
        break
    else:
        conversao = ''.join(calculo)
        try:
            resultado = eval(conversao)
        except ZeroDivisionError:
            print('Não é possível dividir por zero.')
            resultado = None
        print(f'resultado = {resultado}')
