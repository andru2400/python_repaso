import random

IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   x|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   x|x  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   x|x  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   x|x  |
    |   |
   x    |
        =========''', '''

    +---+
    |   |
    O   |
   x|x  |
    |   |
   x x  |
        =========''', '''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('--- * --- * --- * --- * --- * --- ')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: '))
        letter_indexes = []

        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('!Perdiste, La palabra correcta es {}'.format(word))
                break
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter
            letter_indexes = []

        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('!Felicidades, Ganaste. la palabra es. {}'.format(word))
            break


if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    print("                   _.+sd$$$$$$$$$bs+._                   ")
    print("               .+d$$$$$$$$$$$$$$$$$$$$$b+.               ")
    print("            .sd$$$$$$$P^*^T$$$Ppppppptttttttb            ")
    print("          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          ")
    print("        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        ")
    print("       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       ")
    print("     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     ")
    print("    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    ")
    print("   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   ")
    print("  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  ")
    print("  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  ")
    print(" :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; ")
    print(" $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ ")
    print(":$$$$$$$b            `*T$$$s                      :$$$$$;")
    print(":$$$$$$$$b.                                        $$$$$;")
    print("$$$$$$$$$$$b.                                     :$$$$$$")
    print("$$$$$$$$$$$$$bs.                                 .$$$$$$$")
    print("$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$")
    print(":$$$$$$$$$$$$$Pqqq eee                     fffsdssssssssp")
    print(":$$$$$$$$$$$$P     TP^hhT$bss++.._____..++sd$$$$$$$$$$$$;")
    print(" $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ ")
    print(" :$$$$$$$$$$$$b.           `*T$$P^*777llllT$$$$$$$$$$$$; ")
    print("  $$$b       `T$b+                        :$$$$$$$BUG$$  ")
    print("  :$Ps                                   ._.$$$$$$$$$$$  ")
    print("   \                            `*TP*     d$$P*******$   ")
    print("    \                                    :$$P'      /    ")
    print("     \                                  :dP'       /     ")
    print("      `.                               d$P       .'      ")
    print("[bug]   `.                             `'      .'        ")
    print("          `-.                               .-'          ")
    print("             `-.                         .-'             ")
    print("                `*+-._             _.-+*'                ")
    print("                      `a77777-*aa}                       ")
    run()
