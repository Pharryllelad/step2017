import random
user_wins = 0
computer_wins = 0
for i in range (5):
 random_num = random.randint (1, 3)
 
 choice = input("Enter Rock,Paper, or Scissors ==>")
 
 if choice == "rock":
  choice =(1)
 if choice == "paper":
  choice =(2)
 if choice == "scissors":
  choice =(3)

 if choice == 1 and random_num ==3:
  print(" You Win!")
  user_wins = user_wins + 1
 if choice == 2 and random_num == 1:
  print( "You win")
  user_wins = user_wins + 1
 if choice == 3 and random_num == 2:
  print(" You win!")
  user_wins = user_wins + 1
 if choice == 3 and random_num == 1:
  print(" You Lose")
  computer_wins = computer_wins + 1
 if choice == 1 and random_num == 2:
  print(" You lose")
  computer_wins = computer_wins + 1
 if choice == 2 and random_num == 3:
  print(" You lose!")
  computer_wins = computer_wins + 1
 
 if choice == random_num:
     print(" It's a Tie!")
     
 if random_num == 1:
  print("They chose rock")
 if random_num == 2:
  print("They chose paper")
 if random_num == 3:
  print("They chose scissors")
if user_wins < computer_wins:
  print("The computer won more games!")
  print(computer_wins)
elif computer_wins < user_wins:
  print("The User wins!")
  print(user_wins)
else:
  print("You guys won the same number of games")