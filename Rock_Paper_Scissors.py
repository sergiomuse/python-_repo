#import random
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

#computer = random.randint(0, 2)
computer =0
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