import random
import os

class Wordle:

    def __init__(self):
        
        self.validWords = self.getValidWords()
        self.secret_word = random.choice(self.validWords)
        self.guesses = 0
        self.maxGuesses = 5
        self.correctAnswer = False
        self.guessHistory = []
        self.startGame()


    def getValidWords(self):
        validWords = []
        with open('wordle_ord.txt', 'r') as file:
            while True:
                word = file.readline()
                if word == "":
                    break
                validWords.append(word[0:5])
        
        return validWords
    
    def checkWord(self, word):
        return word in self.validWords
    
    def makeGuess(self):
        # Take guess input from player and checks whether a valid guess or not
        guess = input('Input your guess (Write a five letter word):').lower()


        # Keeps track of guesses so far.
        self.guessHistory.append([guess])
        self.guesses += 1

        # Checks if the guess just made was a correct guess.
        if guess == self.secret_word:
            self.correctAnswer = True
        
    def printGame(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print('Current wordle board:\n')

        # Loops through the guesses made so far and prints them out such that they can be analysed for making the next guess
        print("_____________________________________________________________________________\n")
        for index, guess in enumerate(self.guessHistory):
            text = ""
            for i, letter in enumerate(list(guess)):
                if letter == list(self.secret_word)[index]:



        print("_____________________________________________________________________________")
        print(f'\nYou have {self.maxGuesses-self.guesses} guesses left.')
       

    def startGame(self):
        os.system('cls' if os.name=='nt' else 'clear')
        print("Welcome to wordle, you have 5 tries to guess the right word")

        while (self.guesses < self.maxGuesses and not self.correctAnswer):
            self.makeGuess




if __name__ == "__main__":
    wordle = Wordle()