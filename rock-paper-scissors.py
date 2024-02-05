from random import *

choices = ['rock', 'paper', 'scissors']
computer_points = 0
player_points = 0

for i in range(5):
    print("----------------------------------------")
    user_choice = input("Enter rock, paper or scissors: ").lower()
    computer_choice = choice(choices)

    if user_choice == computer_choice:
        print("Draw")
    
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print("You lose!")
            computer_points += 1
        else:
            print("You win!")
            player_points += 1
    
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("You win!")
            player_points += 1
        else:
            print("You lose!")
            computer_points += 1
    
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print('You win!')
            player_points += 1
        else:
            print('You lost!')
            computer_points += 1

print("----------------------------------------")

print(f"Computer points: {computer_points}")
print(f"Your points: {player_points}")

print("----------------------------------------")

if computer_points > player_points:
    print("You lost the match")
elif computer_points == player_points:
    print("Draw!")
else:
    print("You won the match!")