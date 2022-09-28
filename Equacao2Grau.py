import math as m


delta    = lambda a, b, c: m.pow(b, 2) - (4*a*c)
bhaskara = lambda a, b, delta: (
                                (-b + m.sqrt(delta)) / (2 * a), 
                                (-b - m.sqrt(delta)) / (2 * a))


def armazenar(arg):
    try: 
        return int(input(arg))
    except:
        return float(input(arg))



if __name__ == '__main__':

    coeficiente = ['a', 'b', 'c']                                                            
    pergunta = [f'Declare o valor de {sequencia}:' for sequencia in coeficiente]
    ciclo = ''

    while ciclo != 'p':
        print('raizes de uma equação do 2º grau')
        pergunta_calculo = [armazenar(p) for p in pergunta]
        
        if pergunta_calculo[0] <= 0:
            print('Esta não é uma equação do 2º grau.')

        else:
            x1_x2 = bhaskara(pergunta_calculo[0], pergunta_calculo[1], delta(pergunta_calculo[0], pergunta_calculo[1], pergunta_calculo[2]))
            
            mostrar = [f'x{e+1}: {valor}' for e, valor in enumerate(x1_x2)]
            print('\n'.join(mostrar))

        ciclo = input('Digite "p" caso queira parar, pressione <Enter> para continuar.').strip().lower()
