from random import randint

play = ["Rock", "Paper", "Scissors"]

computer = play[randint(0, 2)]
print('Computer: {}.format(computer))

<<<<<<< HEAD
player = input(Rock, Paper, Scissors)
print('player: {}.format(player))

      
=======
player = "Paper"
print('player: {}.format(player))

if player == computer:
  print("Tie!")
elif player == "Rock":
  if computer == "Scissors":
    
>>>>>>> compare
