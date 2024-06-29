import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps_map = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

my_chose = int(input())

pc_chose = random.randint(0,2)


print(rps_map[my_chose])
print("Computer chose:")
print(rps_map[pc_chose])


if my_chose == pc_chose:
    print("It's a draw")
elif my_chose == 0 and pc_chose == 2:
    print("You Win")
elif my_chose == 1 and pc_chose == 0:
    print("You Win")
elif my_chose == 2 and pc_chose == 1:
    print("You Win")
else:
    print("You Lose")
    