from day11_art import logo
from os import system
import random


your_cards = []
current_score = 0
final_score = 0
computer_cards = []
computer_score = 0
another_card = True
want_play = True


def verify_ace(cards):
    if 11 in cards and count_score(cards) > 21:
        cards[cards.index(11)] = 1



def add_card(cards):
    score_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    
    choise_card = random.choice(score_cards)
    cards.append(choise_card)
    
    
    
def count_score(cards):
    score = 0
    for n in cards:
        score += n
    return score



def round_card(my_cards, pc_cards, my_turn, pc_turn):
    for _ in range(my_turn):
        add_card(my_cards)
    for _ in range(pc_turn):
        add_card(pc_cards)
    
    
    

def verify_score(my_cards, pc_cards):
    my_score = count_score(my_cards)
    pc_score = count_score(pc_cards)    
    print(f"   Your final hand: {my_cards}, final score: {my_score}")
    print(f"   Computer's final hand: {pc_cards}, final score: {pc_score}") 
    if my_score > 21:
        print("You went over. You Lose 😭")
    elif pc_score > 21:
        print("Opponent went over. You win 😁")     
    elif my_score == pc_score:
          print("Draw 🙃")
    elif my_score > pc_score:
        print("You win 😀")
    else:
        print("You lose 😤")
        
        
        


while want_play:
    _want_play = input("Do you want to play a game of Blackjack? Type 'y or 'n': ")    
    if _want_play == 'n':
        want_play = False
        break
    your_cards = []
    computer_cards = []  
              
    system('cls') 
    print(logo)
    
    round_card(my_cards=your_cards, pc_cards=computer_cards, my_turn=2, pc_turn=2)
    print(f"   Your cards: {your_cards}, current score: {count_score(your_cards)}")
    print(f"   Computer's first card: {computer_cards[0]}")
    
    if count_score(computer_cards) == 21:
        print("Lose, opponent has Blackjack 😱")
        break
    
    while count_score(your_cards) < 21:
        _another_card = input("Type 'y' to ge another card, type 'n' to pass: ")
        if _another_card == 'n':
            another_card = False
            break
        round_card(my_cards=your_cards, pc_cards=computer_cards, my_turn=1, pc_turn=0)
        print(f"   Your cards: {your_cards}, current score: {count_score(your_cards)}")
        print(f"   Computer's first card: {computer_cards[0]}")
        verify_ace(your_cards)
    
    if count_score(your_cards) > 21:
        verify_score(your_cards, computer_cards)
        continue
        
    while count_score(computer_cards) <= 16:
        round_card(my_cards=your_cards, pc_cards=computer_cards, my_turn=0, pc_turn=1)
        print(f"   Your cards: {your_cards}, current score: {count_score(your_cards)}")
        print(f"   Computer's first card: {computer_cards[0]}")
        verify_ace(computer_cards)
            
    verify_score(your_cards, computer_cards)
        
            
    
    
    


    
        
    
        
    
