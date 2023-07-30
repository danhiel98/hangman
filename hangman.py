import random

words = [
        "Computadora", "Escuela", "Calendario", "Nuez", "Oruga", 
        "Dulce", "Margarita", "Pez", "Caldero", "Marruecos"
        ]

def hangman(word):
    wrong = 0
    stages = [
            "",
            "_______   ",
            "|       ",
            "|   |   ",
            "|   O   ",
            "|  /|\  ",
            "|  / \  ",
            "|       "
            ]
    
    tried = list()
    rletters = list(word.lower())
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hang man")

    while wrong < len(stages) - 1:
        print("\n")
        print(tried)
        msg = "Guess a letter:"
        char = input(msg)

        tried.append(char)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was \"{}\"".format(word))

rnd = random.randint(0,9)

hangman(words[rnd])
