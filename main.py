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
game_images = [rock,paper,scissors]
persons_choice = int(input("what will u Choose -> 0 for rock,1 for paper or 2 for scissor\n"))
if persons_choice > 2 or persons_choice < 0:
  print("Invalid Input!")
else:
  print(game_images[persons_choice])

computers_choice = random.randint(0,2)
print("Computer Chose:\n")
print(game_images[computers_choice])

if persons_choice > 2 or persons_choice < 0:
  print("Please enter a valid input!")

elif persons_choice == computers_choice:
  print("it's a draw")
elif persons_choice == 0 and computers_choice == 2:
  print("You win!")
elif persons_choice == 2 and computers_choice == 0:
  print("You Lose!")
elif persons_choice > computers_choice:
  print("You Win!")
elif computers_choice > persons_choice:
  print("You Lose!")
