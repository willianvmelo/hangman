# Jogo da forca com Python

# importando pacotes
import random
from hangman import Hangman


# Função para ler uma palavra de forma aleatória do banco de palavras


def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()

# Método Main execução do programa.


def main():

    # Instancia da classe Hangman

    game = Hangman(rand_word())

    while not game.hang_over():
        game.hang_status()
        entry = input('\nDigite uma letra:')
        game.guess(entry)
    game.hang_status()

    if game.hang_won():
        print('Você Venceu!')
    else:
        print('Você perdeu!')
        print(f'A palavra era {game.word}')

# Executando o programa


if __name__ == '__main__':
    main()
