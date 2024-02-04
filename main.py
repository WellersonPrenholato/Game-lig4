import math

from jogada import registraJogada
from pontuacao import *
from option_modes import *

##########################################################

if __name__ == "__main__":

    print ("Informe o modo do jogo que deseja jogar:")
    print("1 - Preencha todas as posições. ")
    print("2 - Quem fizer o primeiro ponto ganha.")

    entrada = int(input("Informe: "))
    escreveTitle()

    if entrada == 1:
        modeAllPositions()
    elif (entrada == 2):
        modeOneGold()
    else:
        print("O valor informado não corresponde as opções informadas.\n")
        exit()