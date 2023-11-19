import random

def choose_word():

    words = ["python", "hangman", "technologie", "development", "gifi", "wolf", "louisan"]
    return random.choice(words)


def hide_word(word, hiding_letter):
    hideword =""
    for letter in word:
        if letter in hiding_letter:
            hideword += letter + " "
        else:
            hideword += "_ "
    return hideword


def choose_letter():
    letter = input("Choose a letter : ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print("please enter a valid letter")
        return choose_letter()
    return letter


def hangman():

    the_word = choose_word()
    hiding_letter = set()
    attemps = 6

    print("Welcome to the Hangman game ! ")

    while attemps > 0:
        actual_word = hide_word(the_word, hiding_letter)
        print("\nWord to devinies : ", actual_word)
        print("Remaining attemps : ", attemps)

        letter = choose_letter()

        if letter in hiding_letter:
            print("You already have this letter.")
        elif letter in the_word:
            print("You discover a letter !")
            hiding_letter.add(letter)
            if len(hiding_letter) == len(set(the_word)):
                print("Congratulation, you discover the word : ", the_word)
                break
        else:
            print("This letter aren't in this word.")
            attemps -= 1 
    if attemps == 0:
        print("\nGame Over ! The word was : ", the_word)


hangman()