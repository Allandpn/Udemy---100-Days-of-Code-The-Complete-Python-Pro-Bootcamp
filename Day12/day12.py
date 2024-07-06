from day12_art import logo
import random


NUMBER = random.randint(1,100)



def calc(n_attempts):      
    while n_attempts > 0:
        print(f"You have {n_attempts} attenmpts remaining to guess the number")  
        guess = int(input("Make a guess: "))            
        if guess > NUMBER:
            print("Too high.\nGuess again.")
        elif guess < NUMBER:
            print("Too low.\nGuess again.")
        else:
            print(f"You got it! The ansewer was {NUMBER}")
            return
        n_attempts -= 1
    print("You've run out of guesses, you lose.")
        
        

def start():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    print("Pssst, the correct answer is 72")   
    q1 = False
    while not q1:
        difficult = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficult == "easy":            
            calc(10)
        elif difficult == "hard":
            calc(5) 
        else:
            q1 = True
    
    
      
start()


