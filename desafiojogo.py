import time
import random

def escolhe_jogo():
    print("*********************************")
    print("**Jogo: Pedra - Papel - Tesoura***")
    print("*********************************")
    
    pontos_maquina = 0
    pontos_jogador = 0
    
    while True:
   
        maquina = (random.randrange(1,151))
        if (1 <= maquina < 50):
            maquina="pedra"
        elif (50 <= maquina < 100):
            maquina = "papel"
        elif (100 <= maquina < 151):
            maquina = "tesoura"
        
        time.sleep(1)
        print("Pedra")
        time.sleep(1)
        print("Papel")
        time.sleep(1)
        print("Tesoura")
        
        ##entrada do jogador
        jogador=str(input("Digite Pedra, Papel ou Tesoura\n"))
        jogador=jogador.lower()
       
        ##condições de vitória ou empate
        condicao1 = (jogador == maquina)
        condicao2 = ((jogador == "pedra") and (maquina == "tesoura"))
        condicao3 = ((jogador == "tesoura") and (maquina == "papel"))
        condicao4 = ((jogador == "papel") and (maquina == "pedra"))
        condicao5 = ((maquina == "pedra") and (jogador == "tesoura"))
        condicao6 = ((maquina == "tesoura") and (jogador == "papel"))
        condicao7 = ((maquina == "papel") and (jogador == "pedra"))
        condicao8 = (jogador == "sair")
        condicao9 = (jogador != ("pedra") or ("papel") or ("tesoura"))
       
        ##condições com mensagens e soma de pontos
        if condicao1:          
            print("Computador: {} Jogador: {}   Empatou!!!".format(jogador,maquina))
        elif condicao2 or condicao3 or condicao4:
            pontos_jogador=pontos_jogador+10
            print("Computador: {} Jogador: {}   Jogador venceu!\nMais 10 pontos\nPontos jogador {}".format(maquina,jogador,pontos_jogador))
        elif condicao5 or condicao6 or condicao7:
            pontos_maquina=pontos_maquina+10
            print("Computador: {} Jogador: {}  Computador venceu!\nMais 10 pontos\nPontos computador {}".format(maquina,jogador,pontos_maquina))
        elif condicao8:
            break
        elif condicao9:
            print("Digite Pedra, Papel ou Tesoura para jogar")
    print("Pontos Computador - {} Pontos Jogador - {}".format(pontos_maquina,pontos_jogador))
if __name__=="__main__":
    escolhe_jogo()