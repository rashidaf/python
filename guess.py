shownWord = ["_","_","_","_"]
word = "wavy"

print("You are playing: Hangman")

tries = 0
glist = []

guess = input("Type a letter to start guessing, you have 5 guesses")

if guess.isnumeric():
    print("There is no numbers in a word, try again")

while tries < 4:
    for index in range (len(word)):
        if(word[index] == guess):
            shownWord[index] = guess
            print(shownWord)
            guess = input ("Good, keep guessing")

        if (guess not in word):
            tries +=1
            print("No, that's not correct, you have", 5 - tries, "left")
            print(shownWord)
            guess = input("Try again:")
            break

    if (tries == 4):
        print("Sorry, you lose")
