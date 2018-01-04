tab = []
def mostraTabuleiro (tab):
    qtVez = 6
    print("   ",1,"-",2,"-",3,"-",4,"-",5,"-",6)
    print("  _________________________")
    for i in range(qtVez) :
         print (i,"|", tab [i+5][6], "|", tab [i+10][11], "|", tab [i+15][16], "|", tab [i+20][21], "|", tab[i+25][26], "|", tab[i+30][31], "|\n")












         

def validaPreenchimento(tab):
    lista = ["A","B","C","D","E","F"]
    for x in range(36):
        tab.append([random.choice(lista)])
        while(validaPreenchimento == False):
            [i].tab.append([random.choice(lista)])

def preencher1(tab,posicao):
    if((tab[posicao - 1] == tab[posicao]) and (tab[posicao - 2] == tab[posicao])):
        return False
    elif((tab[posicao - 1] == tab[posicao]) and (tab[posicao + 1] == tab[posicao])):
        return False
    elif((tab[posicao + 1] == tab[posicao]) and (tab[posicao + 2] == tab[posicao])):
        return False
    else:
        return True


    

    
            

