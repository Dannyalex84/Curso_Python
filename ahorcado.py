import os
import random


def word():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        words = [line for line in f]  # List comprehensions
    wordrandom = (random.choice(words)).upper()
    return wordrandom


def lenword(word):
    len_word = len(word)-1
    presentation = ["_ "]*len_word
    return presentation


def changelarge(hiddenword, letter, index):
    hiddenword[index] = letter
    return hiddenword


def imprimirpantalla(lifes):
    print("="*20+" Bienvenido al Hangman Game "+"="*20)
    my_list_ASCII = ['''
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                  ========= ''', '''
                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                  ========= ''', '''
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                  ========= ''', '''
                    +---+
                    |   |
                    O   |
                   /|   |
                        |
                        |
                  ========= ''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                  ========= ''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                  ========= ''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                  ========= ''']
    my_list_ASCII = my_list_ASCII[::-1]
    print(my_list_ASCII[lifes])


def play():
    selectword = word()
    large = lenword(selectword)

    hits = 0
    objective = len(selectword)-1
    lifes = 6
    usedletters = []

    while lifes > 0 and hits < objective:
        imprimirpantalla(lifes)
        print("")
        print("Adivine la siguiente palabra. La misma cuenta con " +
              str(len(selectword)-1)+" caracteres.")
        print(*large, sep=" ")
        print("")
        letter = input("Ingrese una letra: ").upper()
        assert letter.isalpha(), "Debe introducir una letra. No números"
        while len(letter) != 1:
            letter = input(
                "Ingreso mas de un dígito. Ingrese solo un dígito: ").upper()
            assert letter.isalpha(), "Debe introducir una letra. No números"
        while letter in usedletters:
            letter = input(
                "Ingreso una letra repetida. Ingrese otra que no haya usado: ").upper()
        usedletters.append(letter)
        print("Las letras usadas hasta aquí son: ")
        print(*usedletters, sep=" ")
        hitsbefore = hits
        for i in range(0, len(selectword)-1):
            if selectword[i] == letter:
                hits += 1
                print("Excelente. Ha acertado! Ha sumado 1 punto. Quedan " +
                      str(objective-hits)+" letras por encontrar.")
                large = changelarge(large, letter, i)

        if hitsbefore == hits:
            lifes -= 1
            print(
                "No se encontró la letra elegida. Usted ha perdido una vida. Le quedan: "+str(lifes)+" vidas.")

        input("Presiones Enter para continuar: ")
        os.system("cls")

    if hits == objective:
        imprimirpantalla(lifes)
        print("¡¡¡Felictaciones!!! Usted ha ganado el juego.")
    if lifes == 0:
        imprimirpantalla(lifes)
        print("Game Over. Vuelva a intentarlo mas tarde")


if __name__ == '__main__':
    play()