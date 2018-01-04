import random

# Tratamento de erro para perguntas de SIM ou NÃO #
def entrada (pergunta):
    if(str.lower(pergunta) == "sim"):
        return True
    elif(str.lower(pergunta) == "não"):
        return False
    else:
        if(str.lower(pergunta) != "sim") and (str.lower(pergunta) != "não"):
            pergunta2 = input ("Inválido!\nPor favor, digite apenas 'sim' ou 'não' : ")
            return entrada(pergunta2)
       
# Boas Vindas ao jogo #
def boasVindas ():
 print(""" ~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~~
| * BEM VINDO AO JOGO TRIPLE!! * |
|                                |
|         DIVIRTA-SE :D          |                               
 ~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~~ """)

# Regras do jogo #
def regras():
 print("""\n ~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
|                              *REGRAS DO JOGO TRIPLE!*                                    |
|-> O jogo é individual.                                                                   |
|-> O tabuleiro foi representado por LETRAS DO ALFABETO(A, B, C, D, E e F).                |
|-> O jogo possui 6 colunas (verticais) e 6 linhas (horizontais).                          | 
|-> A cada jogada, o jogador terá que escolher a linha e coluna da letra qual deseja       |
|movimentar.                                                                               |
|-> O jogador deverá informar o movimento desejado: para 'cima' ou para 'baixo',           |
|para 'esquerda' ou para 'direita'.                                                        |
|-> O objetivo do jogo é que seja formado uma sequência de TRÊS LETRAS IGUAIS              |
|na horizontal(triple), com isso, O JOGADOR GANHARÁ 20 PONTOS!                             |
|-> Os triples só valem na horizontal e devem ser formados por exatamente                  |
|TRÊS LETRAS IGUAIS.                                                                       |
|-> O jogo encerra quando você tiver feito exatamente 40 jogadas.                          |         
|-> BOA SORTE! :D                                                                          |
 ~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~~~-~-~-~-~-~-~-~-~-~-~-~-~-~-~""")

# Função feita para criação de sublistas de elementos aleatórios, testando de 3 em 3 para verificar caso de triple #
def criarTabuleiro():
    tab = ["A","B","C","D","E","F"]
    tabu = []
    for x in range(6):
        linha = []
        for i in range(6):
            linha += random.choice(tab)
        for q in range(4):
            if(linha[q]==linha[q+1])and(linha[q+1]==linha[q+2]):
                escolhaLetra = random.choice(tab)
                linha[q+1] = escolhaLetra
        tabu += [linha]
    return tabu


# Função criada para exibir o tabuleiro #
def mostraTabuleiro (tab):
    qtVez = 6
    print("   ",1,"-",2,"-",3,"-",4,"-",5,"-",6)
    print("  _________________________")
    for mostra in range(qtVez) :
         print (mostra+1,"|", tab [mostra][0], "|", tab [mostra][1], "|", tab [mostra][2], "|", tab [mostra][3], "|", tab[mostra][4], "|", tab[mostra][5], "|\n")

# Tratamento para transformar str. em int. e tratamentos para números acima de 6 e outros caracteres #
def tratamentoLinhaOuColuna (entrada):
    if (entrada == "1") or (entrada == "2") or (entrada == "3") or (entrada == "4") or (entrada == "5") or (entrada == "6"):
        return int(entrada)
    else:
        if(entrada != "1") or (entrada != "2") or (entrada != "3") or (entrada != "4") or (entrada != "5") or (entrada != "6"):
          pergunta = (str.lower(input ("Inválido!\nPor favor, digite apenas NÚMEROS entre '1' a '6': ")))
          return tratamentoLinhaOuColuna(pergunta)
            
# Recebe os determinados dados para realizar a troca dos elementos #
def movimentoDireita (lista, linha, coluna,troca):
        direita = lista[linha-1][coluna]
        lista[linha-1][coluna-1] = direita
        lista[linha-1][coluna] = troca
        return lista
    
def movimentoEsquerda (lista, linha, coluna, troca):
        esquerda = lista[linha-1][coluna-2]
        lista[linha-1][coluna-1] = esquerda
        lista[linha-1][coluna-2] = troca
        return lista
    
def movimentoBaixo (lista, linha, coluna, troca):
        baixo = lista[linha][coluna-1]
        lista[linha-1][coluna-1] = baixo
        lista[linha][coluna-1] = troca
        return lista
   
def movimentoCima (lista, linha, coluna, troca):
        cima = lista[linha-2][coluna-1]
        lista[linha-1][coluna-1]= cima
        lista[linha-2][coluna-1]= troca
        return lista

# As possibilidades de realizar os movimentos e tratando os erros que podem apresentar nas linhas e colunas 1 e 6. #
def movimentacao (linha, coluna, posicao):
    
    if(linha == 1):
        if(coluna == 1):
            if(posicao == "baixo")or(posicao == "direita"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
        elif(coluna >=2)and(coluna <=5):
            if(posicao == "baixo")or(posicao == "esquerda")or(posicao == "direita"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
        elif(coluna == 6):
            if(posicao == "baixo")or(posicao == "esquerda"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
            
    elif(linha >=2)and(linha <=5):
        if(coluna >=2)and(coluna <=5):
            if(posicao == "direita")or(posicao == "baixo")or(posicao == "cima")or(posicao == "esquerda"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)  
        elif(coluna == 1):
            if(posicao == "cima")or(posicao == "baixo")or(posicao == "direita"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
            
        elif(coluna == 6):
            if(posicao == "baixo")or(posicao == "esquerda")or(posicao == "cima"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
    elif(linha == 6):
        if(coluna == 1):
            if(posicao == "cima") or (posicao == "direita"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
        elif(coluna >=2)and(coluna <=5):
            if(posicao == "cima")or(posicao == "esquerda")or(posicao == "direita"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
        elif(coluna == 6):
            if(posicao == "cima")or(posicao == "esquerda"):
                return posicao
            else:
                posicao = str.lower(input("Inválido!\nPor favor, digite um movimento válido: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? "))
                return movimentacao(linha,coluna,posicao)
            
# Função criada para controle de pontos, testar se os elementos de determinados índices(letras) são iguais e a partir disso fazer uma substituição por novas letras #
def controle(tab):
    quantPontos = 0
    for x in range(6):
        lista = ["A","B","C","D","E","F"]
        random.shuffle(lista)
        if(tab[x][0]==tab[x][1])and(tab[x][1]==tab[x][2]):
            for i in range(3):
                    tab[x][i]=lista[i]
                    quantPontos += 7
            quantPontos-=1
    for x in range(6):
        lista = ["A","B","C","D","E","F"]
        random.shuffle(lista)
        if(tab[x][1]==tab[x][2])and(tab[x][2]==tab[x][3]):
            for i in range(3):
                    tab[x][i+1]=lista[i]
                    quantPontos += 7
            quantPontos-=1
    for x in range(6):
        lista = ["A","B","C","D","E","F"]
        random.shuffle(lista)
        if(tab[x][2]==tab[x][3])and(tab[x][3]==tab[x][4]):
            for i in range(3):
                    tab[x][i+2]=lista[i]
                    quantPontos += 7
            quantPontos-=1
    for x in range(6):
        lista = ["A","B","C","D","E","F"]
        random.shuffle(lista)
        if(tab[x][3]==tab[x][4])and(tab[x][4]==tab[x][5]):
            for i in range(3):
                    tab[x][i+3]=lista[i]
                    quantPontos += 7
            quantPontos-=1
            
    return tab,quantPontos
