# hangman-closure.py
def make_hangman(secret_word):
    guesses = []
    
    def hangman_closure(letter):
        guesses.append(letter)
        revealed = "".join([c if c in guesses else "_" for c in secret_word])
        print(revealed)
        return "_" not in revealed
    
    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ")
    play = make_hangman(secret)
    
    while True:
        letter = input("Guess a letter: ")
        if play(letter):
            print("You guessed the word!")
            break
