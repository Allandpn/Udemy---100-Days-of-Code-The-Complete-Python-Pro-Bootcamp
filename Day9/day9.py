from os import system
from day9_art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secrect auction program.")

end_bid = False
dict_bit = {}



def find_winner():
    most_bit = 0
    most_name = ''
    for name in dict_bit:
        if dict_bit[name] > most_bit:
            most_bit = dict_bit[name]
            most_name = name
    print(f"The winner is {most_name} with a bid of ${most_bit}")
    
    

while not end_bid:
    name = input("What is your name? ")
    bit = int(input("What's your bid? "))    
    dict_bit[name] = bit   
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")        
    if other_bidders == "yes":
        system('cls')
    else:
        end_bid = True
        find_winner()


        





