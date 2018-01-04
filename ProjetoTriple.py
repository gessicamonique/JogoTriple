import BibliotecaProjeto

printBoasVindas = BibliotecaProjeto.boasVindas ()

# Pergunta inicial e a partir dela vai ser chamada a biblioteca para fazer o tratamento da resposta #
pergunta = input ("Deseja entrar no jogo? Digite 'sim' ou 'não' : ")
tratPergunta = BibliotecaProjeto.entrada(pergunta)

# Se a resposta for 'sim', logo será retornado 'True' para então ser exibido as regras do jogo; 
if (tratPergunta == True):
    BibliotecaProjeto.regras()
# Será feita uma nova pergunta ao usuário se ele deseja sair e a partir disso vai ser chamada a biblioteca novamente para fazer o tratamento da resposta #
    perguntaSair = input ("Você deseja continuar? Digite 'sim' ou 'não': ")
    tratSair = BibliotecaProjeto.entrada(perguntaSair)
    
# Se a resposta for 'sim', logo será retornado 'True' e com isso será feita uma pergunta ao usuário sobre seu nome;
    if(tratSair == True):

        jogador = str.capitalize (input ("Jogador(a), informe seu nome: "))
        print (jogador,", começará o jogo! \n")
# Logo em seguida será exibido o tabuleiro;
        tabuleiro = BibliotecaProjeto.criarTabuleiro()
        BibliotecaProjeto.mostraTabuleiro(tabuleiro)
# E será feita novamente a pergunta se o jogador desejar sair, em que mais uma vez será chamada a biblioteca para realizar o tratamento da resposta #
        opcaoSair = input ("Você deseja continuar? Digite 'sim' ou 'não': ")
        tratSair = BibliotecaProjeto.entrada(opcaoSair)
        quantidadeJogadas = 40
        pontos = 0
        quantPontuacao = 0
        

        while(opcaoSair != "não"):
            quantidadeJogadas -= 1 #Contador das jogadas#

            linha = input ("Qual a linha que deseja mover? Digite entre '1' a '6': ")
            tratamentoLinha = BibliotecaProjeto.tratamentoLinhaOuColuna(linha) # Tratamento utilizado para converter str. para int #
            coluna = input ("Qual a coluna que deseja mover? Digite entre '1' a '6': ")
            tratamentoColuna = BibliotecaProjeto.tratamentoLinhaOuColuna(coluna) # Tratamento utilizado para converter str. para int #
            troca = tabuleiro[tratamentoLinha-1][tratamentoColuna-1] # Pega a posição que o usuário digitar subtraindo 1 para fazer a troca desejada do movimento #
            print ()
            print ("O elemento selecionado foi:", "[",troca,"]","na linha:", tratamentoLinha, "e na coluna:",tratamentoColuna, "\n") #Exibe o elemento selecionado #
            movimento = str.lower(input("Qual o movimento que deseja realizar: 'Direita', 'Esquerda', 'Cima' ou 'Baixo'? ")) 
            comando = BibliotecaProjeto.movimentacao(tratamentoLinha, tratamentoColuna, movimento) # Comandos necessários para realizar o movimento #


            # Comandos necessários para realização da movimentação #
            if(comando == "direita"):
                tabuleiro = BibliotecaProjeto.movimentoDireita(tabuleiro, tratamentoLinha, tratamentoColuna, troca)
            elif(comando == "esquerda"):
                tabuleiro = BibliotecaProjeto.movimentoEsquerda(tabuleiro, tratamentoLinha, tratamentoColuna, troca)
            elif(comando == "baixo"):
                tabuleiro = BibliotecaProjeto.movimentoBaixo(tabuleiro, tratamentoLinha, tratamentoColuna, troca)
            elif(comando == "cima"):
                tabuleiro = BibliotecaProjeto.movimentoCima(tabuleiro, tratamentoLinha, tratamentoColuna, troca)
                
            # Necessário porque a partir da função recebe a substituição por novas letras quando ocorre triple e quantidade de pontos #
            controle, quantPontuacao = BibliotecaProjeto.controle(tabuleiro)   
            BibliotecaProjeto.mostraTabuleiro(tabuleiro) # Exibe o tabuleiro #
            pontos += quantPontuacao # Contador para quantidade de pontos #
            print ("Sua pontuação atual", jogador, "é:", pontos,"!") # Exibir pontuação atual #
            
            # Controla a quantidade de Jogadas e a opção sair # 
            if (quantidadeJogadas > 0):
                opcaoSair = input ("Você deseja continuar? Digite 'sim' ou 'não': ")
                tratSair = BibliotecaProjeto.entrada(opcaoSair)
            else:
                opcaoSair = "não"

        print ("Fim de jogo! Sua pontuação", jogador,"foi:", pontos,"!") # Exibir pontuação caso jogador quiser sair #
