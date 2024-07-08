from day13_art import logo, vs
from day13_data import data
import random


end_game = False
score_player = 0


def choise_option():
    name = ""
    description = ""
    country = ""
    number_choise = random.randint(0, len(data)-1)
    name = data[number_choise]["name"]
    description = data[number_choise]["description"]
    country = data[number_choise]["country"]    
    follower_count = data[number_choise]["follower_count"]    
    return name, description, country, follower_count


def compare_count(follower_count_a, follower_count_b, choise):
    if choise == "A" and int(follower_count_a) > int(follower_count_b):
        return 1
    elif choise == "B" and int(follower_count_a) < int(follower_count_b):
        return 1
    else:   
        return 0
    

def game():
    global end_game
    global score_player
    print(logo)
    select_a = choise_option()
    print(f"Compare A: {select_a[0]}, {select_a[1]}, from {select_a[2]}.")
    print(vs)
    select_b = select_a
    while select_b == select_a:
        select_b = choise_option()
    print(f"Adainst B: {select_b[0]}, {select_b[1]}, from {select_b[2]}.")
    choise = input("Who has more followers? Type 'A' or 'B': ")        
    result = compare_count(follower_count_a=select_a[3], follower_count_b=select_b[3], choise=choise)    
    if result == 1:
        score_player += 1
        print(f"You're right! Current score: {score_player}")
    else:
        print(f"Sorry, that's wrong. Final score: {score_player}")
        play_again = input("Do you want play again? Type 'y' for yes or 'n' for no: ")
        if play_again == "n":
            end_game = True
    
        
while not end_game:
    game()