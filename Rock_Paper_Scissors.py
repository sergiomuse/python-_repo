<<<<<<< HEAD
import random
=======
<<<<<<< HEAD
import random
=======
#import random
>>>>>>> 66370bcc9858b510bd045c170f0ab235b988ef43
>>>>>>> 1de2ca641e7641b5b791ce9850df5d986bfe70bf
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
<<<<<<< HEAD
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


=======

print("Welcome  to game rock, paper or scissors \n")
print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors")

player=int(input())
print("Player")
if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)

computer = random.randint(0, 2)

print("Computer")
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

row1 = ["Draw","You lose","You win"]
row2 = ["You lose","Draw","You lose"]
row3 = ["You lose","You win","Draw"]
map = [row1, row2, row3]
print(player)
print(computer)
resultado =  map [player][computer]

print(resultado)
>>>>>>> 66370bcc9858b510bd045c170f0ab235b988ef43
