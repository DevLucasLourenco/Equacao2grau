import pyautogui as pg
import random
from beautifultable import BeautifulTable
import os
table = BeautifulTable()
table.set_style(BeautifulTable.STYLE_RST)



class selecionar_cor:
    v = '\033[92m'
    x = '\033[91m'



def armazenar(arg):
  try:
    return int(input(arg))
  
  except:
    return float(input(arg))



def jogadores():
    qtde_jogadores = int(input('Quantas pessoas jogarão?'))
    texto = [f'Informe o nome do Jogador {e + 1}:' for e, sequencia in enumerate(range(qtde_jogadores))]
    jogadores = [input(t).strip().title() for t in texto]

    return jogadores

  

def script():
    valor_inicial = 1
    valor_final = (10 + 1) # permaneça com o "+1" para com que seja selecionado também o último número que foi posto na variável

    numero_randomizado = random.randrange(valor_inicial, valor_final)
    table.columns.header = ['Nome','Valor','Status','']

    contador = 0
    marcador = 0
    while marcador < 1:

        texto2 = [f'Declare um valor entre {valor_inicial} e {valor_final},  {nome}' for nome in players]
        numero_informado = [armazenar(t2) for t2 in texto2]

        relacao_jog_num = dict(zip(players, numero_informado))

        for nome, valor in relacao_jog_num.items():
            if valor == numero_randomizado:
                table.rows.append([nome, valor, selecionar_cor.v + '✓','Correto'])
                marcador += 1

            elif valor != numero_randomizado:
                if valor < numero_randomizado:
                    table.rows.append([nome, valor, selecionar_cor.x + 'X','Acima'])
                else:
                    table.rows.append([nome, valor, selecionar_cor.x + 'X','Abaixo'])
        contador += 1
        print(table)
        table.rows.clear()
        print(f"{contador}º tentativa" + '\n' * 2)
    


enter = input('Pressione <ENTER> para iniciar...')        
ciclo = ''
while ciclo != 'n':
            
    players = jogadores()
    print('Lista de Jogadores:\n' + '\n'.join(players)+'\n'*2)

    script()
    ciclo = input('Deseja jogar novamente? (S/N))').lower()
    