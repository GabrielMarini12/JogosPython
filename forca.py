import random

#função criada para usar o arquivo junto com outros arquivos
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

    #abrindo o arquivo
    arquivo = open("JOGOS_ALURA/palavras.txt", "r")
    #criando uma lista vazia
    palavras = []

    #para cada linha dentro do arquivos
    for linha in arquivo:
        #tratando o /n depois de cada palavra do arquivo
        linha = linha.strip()
        #vai adicionar uma linha(palavra, pois o arquivo é uma palavra em cada linha)
        palavras.append(linha)

    #fechando o arquivo
    arquivo.close()
    #sortendo o número aleatório da lista para pegar uma palavra, pois é através do indice
    #len - devolve o tamanho total da lista
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    # usa o _ para cada letra dentro da palavra secreta
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    #print(len(palavra_secreta)) = mostra a quantidade de letras da palavra secreta
    
    print(letras_acertadas)
    #enquanto não se enforcou e não acertou (False and False)
    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        #upper - tratando letras minusculas e maiusculas, para aceitar os 2 tipos
        #strip - tratando os espaços caso o usuário digite antes da letra
        chute = chute.strip().upper()
        if(chute in palavra_secreta):
            #index define a posição da letra, inicia em 0
            index = 0
            #para cada letra dentro da minha palavra secreta
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                #serve para registrar a posição caso tenha mais de uma letra igual na palavra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6 
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo!")

#verificando se é o progarama principal rodando, se for, vai executar direto o programa da forca (principal)
#se não for, vai executar primeiro o programa principal (o que estiver rodando).
if(__name__ == "__main__"):
    jogar()