#importando os arquivos para poder chamar as funções criadas neles
import forca
import adivinhacao

def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        #chamando a função para executar o arquivo
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        #chamando a função para executar o arquivo
        adivinhacao.jogar()

#verificando se é o progarama principal rodando, se for, vai executar direto o programa de jogos (principal)
#se não for, vai executar primeiro o programa principal (o que estiver rodando).
if(__name__ == "__main__"):
    escolhe_jogo()