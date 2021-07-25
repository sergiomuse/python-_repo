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
game_images = [rock, paper, scissors]
print("Welcome to game Rock, Paper or Scissor")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player = int(input())
print("Player")
print(game_images[player])
computer = random.randint(0,2)
print("Computer")
print(game_images[computer])

row1 = ["Draw","You lose","You win"]
row2 = ["You win","Draw","You lose"]
row3 = ["You lose","You win","Draw"]
map = [row1, row2, row3]

resultado = map [player][computer]
print(resultado)


