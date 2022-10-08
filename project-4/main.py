import random
rock = '''
    _______
----'   ____)
      (_____)
      (_____)
      (____)
----.__(___)
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

#print(scissors)
game_images=[rock, paper, scissors]
player_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_input>=3 or player_input<0:
  print("invalid number")
else:
  print(game_images[player_input])
  computer_chose = random.randint(0,2)
  print("computer chose: ")
  print(game_images[computer_chose])
  if player_input==0 and computer_chose==2:
    print("you win!!")
  elif player_input==2 and computer_chose==0:
    print("you lose")
  elif computer_chose>player_input:
    print("you lose")
  elif computer_chose<player_input:
    print("you win!")
  elif computer_chose==player_input:
    print("It's a draw!")


