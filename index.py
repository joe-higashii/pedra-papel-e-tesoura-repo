# # #etapa1-escolha-do-usuario

# # print("Escolha: 1 para Pedra, 2 para Papel e 3 para Tesoura")

# # escolha = int(input("Sua hora de escolher: "))

# # if escolha ==1:
# #     nome_escolha = "Pedra"
# # elif escolha ==2:
# #     nome_escolha = "Papel"
# # else:
# #     nome_escolha = "Tesoura"

# # #print("Escolha do usuário: " + nome_escolha)

# # # if condicao1:
# # #     o que fazer caso a condicao1 seja satisfeita
# # # elif: condicao2:
# # #     o que fazer caso a condicao2 seja satisfeita
# # # elif: condicao3:
# # #     o que fazer caso a condicao3 seja satisfeita
# # # elif: condicao4:
# # #     o que fazer caso a condicao4 seja satisfeita
# # # else:
# # #     o que fazer caso a condicao nao seja satisfeita

# # #etapa2-escolha-do-computador

# # # teste = 0

# # # while teste <= 5:
# # #     print(teste)
# # #     teste = teste + 1

# # import random

# # escolha_pc = random.randint(1,3)

# # while escolha == escolha_pc:
# #     escolha_pc == random.randint(1,3)

# # if escolha_pc == 1:
# #     nome_escolha_pc = "Pedra"
# # elif escolha_pc == 2:
# #     nome_escolha_pc = "Papel"
# # else:
# #     nome_escolha_pc = "Tesoura"

# # #print("Escolha do computador é: " + nome_escolha_pc)

# # #etapa3-confronto-usuario-computador

# # print(nome_escolha, "vs", nome_escolha_pc)

# # if ((escolha == 1 & escolha_pc == 2) or (escolha == 2 & escolha_pc == 1)):
# #     print("Papel Vence!")
# #     result = "Papel"
# # elif ((escolha == 1 & escolha_pc == 3) or (escolha == 3 & escolha_pc == 1)):
# #     print("Pedra Vence!")
# #     result = "Pedra"
# # else:
# #     print("Tesoura Vence!")
# #     result = "Tesoura"

# # if result == nome_escolha:
# #     print("<==== Você Venceu!!! :) ====>")
# # else:
# #     print("<==== Computador Venceu!!! :( ====>")

# #etapa4-fazer-um-jogo-repetitivo

# import random

# print("Regras do jogo Pedra, Papel e Tesoura: \n Pedra vs Papel -> Papel Vence \n Pedra vs Tesoura -> Pedra vence \n Papel vs Tesoura -> Tesoura vence \n \n \n")

# repete = True

# while repete == True:
#     #etapa1-escolha-do-usuario
#     print("Escolha: 1 para Pedra, 2 para Papel e 3 para Tesoura")

#     escolha = int(input("Sua hora de escolher: "))
#     print("---------------------")

#     if escolha ==1:
#         nome_escolha = "Pedra"
#     elif escolha ==2:
#         nome_escolha = "Papel"
#     else:
#         nome_escolha = "Tesoura"

#     #etapa2-escolha-do-computador
#     escolha_pc = random.randint(1,3)
#     print("---------------------")

#     while escolha == escolha_pc:
#         escolha_pc == random.randint(1,3)
#         break

#     if escolha_pc == 1:
#         nome_escolha_pc = "Pedra"
#     elif escolha_pc == 2:
#         nome_escolha_pc = "Papel"
#     else:
#         nome_escolha_pc = "Tesoura"
    
#     #etapa3-confronto-usuario-computador
#     print(nome_escolha, "vs", nome_escolha_pc)
#     print("--------------------- \n \n \n")

# if ((escolha == 1 & escolha_pc == 2) or (escolha == 2 & escolha_pc == 1)):
#     print("Papel Vence!")
#     result = "Papel"
# elif ((escolha == 1 & escolha_pc == 3) or (escolha == 3 & escolha_pc == 1)):
#     print("Pedra Vence!")
#     result = "Pedra"
# else:
#     print("Tesoura Vence!")
#     result = "Tesoura"

# if result == nome_escolha:
#     print("<==== Você Venceu!!! :) ====>")
# else:
#     print("<==== Computador Venceu!!! :( ====>")

# ##Perguntar para usuário se quer jogar novamente

# print("Quer jogar novamente? Digite S se sim ou N se não")
# resposta = input()
# if resposta == "N":
#     repete = False

# print("\n Obrigado por jogar!")


from random import choice

play = ["pedra", "papel", "tesoura"]

rule = (("e", "d", "v"), ("v", "e", "d"), ("d", "v", "e"))

text = {
    "e": "    Empatou!",
    "v": "    Parabéns, você venceu!",
    "d": "    Você foi derrotado!",
}

while True:
    h, c = input("Faça a sua jogada: ").lower(), choice(play)

    if h == "sair":
        break

    if h in play:
        print(f"  O computador jogou {c}")
        print(text[rule[play.index(h)][play.index(c)]])
    else:
        print(f"  As jogadas válidas são:\n {play}")