# import random

# def play():
#     user = input("what's your choice'r' for rock, 'p', for paper, 's' scissors\n")
#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return'it\'s a tie'

#     if is_win(user, computer):
#         return 'You won!'
    
#     return 'You lost!, shit'
# def is_win(player, opponent):
#     #return true if player wins
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#         return True
# print(play())



import random

def play():
    usuario = input("Qual sua escolha? 'p' para pedra, 'pa' para papel, 't' para tesoura: ")
    pc = random.choice(['p', 'pa', 't'])

    if usuario == pc:
        return 'Empate!'

    if is_win(usuario, pc):
        return 'Você ganhou!'

    return 'Perdeu, otário!'


def is_win(jogador, maquina):
    # Retorna True se o jogador ganhar
    if (jogador == 'p' and maquina == 't') or \
        (jogador == 't' and maquina == 'pa') or \
        (jogador == 'pa' and maquina == 'p'):
        return True

    return False


print(play())
