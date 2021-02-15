board = ['''
+------
|     |
|
|
|
|
========''', '''

+------
|     |
|     O
|
|
|
========''', '''

+------
|     |
|     O
|     |
|
|
========''', '''

+------
|     |
|     O
|    /|
|
|
========''', '''

+------
|     |
|     O
|    /|\\
|
|
========''', '''

+------
|     |
|     O
|    /|\\
|    /
|
========''', '''

+------
|     |
|     O
|    /|\\
|    / \\
|
========''',



         ]


class Hangman():

    def __init__(self, word):
        self.word = word
        self.letras_corretas = []
        self.letras_erradas = []


# Método para verificar se a letra pertence ou não a palavra buscada no banco de palavras

    def guess(self, letter):
        if letter in self.word and letter not in self.letras_corretas:
            self.letras_corretas.append(letter)
        elif letter not in self.word and letter not in self.letras_erradas:
            self.letras_erradas.append(letter)
        else:
            return False
        return True
# Método para verificar se o jogo terminou

    def hang_over(self):
        return self.hang_won() or (len(self.letras_erradas) == 6)

# Método pra saber se venceu

    def hang_won(self):
        if '*' not in self.hide_word():
            return True
        else:
            return False

# Método para não mostrar a letra no board

    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.letras_corretas:
                rtn += '*'
            else:
                rtn += letter
        return rtn

# Método para acompanhar o status do game

    def hang_status(self):
        print(board[len(self.letras_erradas)])
        print()
        print(f'Palavra: {self.hide_word()}')
        print()
        print('Letras Corretas:')
        for i in self.letras_corretas:
            print(i)
        print()
        print('Letras Erradas:')
        for i in self.letras_erradas:
            print(i)
        print()
