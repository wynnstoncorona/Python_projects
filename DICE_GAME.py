import random
from unittest import result

def main():
    # Keeps track of each player’s score and the count of the program 
    player1count = 0
    player2count = 0
    player1score = 0
    player2score = 0
    # Player 1 while loop
    while player1count < 5:
        player1 = str(input("\nDo you want to role Player 1. Y=yes N=NO: ")).lower()
        # Run player1 input through the player_validation function and assign it to a variable
        input_validation = player_validation(player1)
        # If input_validation returns True we'll print the return statement in else
        # If returns False we bypass this statement to the next if statement
        # The continue statement makes the loop start again  
        if input_validation:
            print(input_validation)
            continue
        # Break the loop if input equals 'n'
        if player1.lower() == "n":
            break
        # Each time we loop add the score to the player1score variable for the total
        player1score += roll_score()
        # Print Player 1 score
        print(player1score)
        # Each time we loop through call program_count if player1 input equals 'y'
        # Add 1 to the player1count variable
        player1count += program_count(player1)
    # Player 2 while loop
    while player2count < 5:
        player2 = str(input("\nDo you want to role Player 2. Y=yes N=NO: ")).lower()
        # Run player2 input through the player_validation function and assign it to a variable
        input_validation = player_validation(player2)
        # If input_validation returns True we'll print the return statement in else
        # If returns False we bypass this statement to the next if statement
        # The continue statement makes the loop start again 
        if input_validation:
            print(input_validation)
            continue
        # Break the loop if input equals 'n'
        if player2.lower() == "n":
            break
        # Each time we loop add the score to the player2score variable for the total
        player2score += roll_score()
        # Print Player 1 score
        print(player2score)
        # Each time we loop through call program_count if player2 input equals 'y'
        # Add 1 to the player2count variable
        player2count += program_count(player2)

    score_logic(player1score, player2score)

def player_validation(input_data):
    try:
        if input_data == 'y' or input_data == 'n':
            return False
        else:
            return "Invalid input please try again"
    except:
        print("Input incorrect")

def roll_score():
    roll = dice()
    score = 0
    if roll % 2 == 0:
        score += roll
    else:
        score -= roll
    return score

def program_count(player_input):
    count = 0
    if player_input.lower() == "y":
        count += 1
    return count

def dice():
    roll_1 = random.randrange(1, 7)
    roll_2 = random.randrange(1, 7)
    roll = roll_1 + roll_2
    print(f'Roll: [{roll_1}] [{roll_2}] = {roll}')
    return roll

def score_logic(score_1, score_2):
    print('\nFinal Score')
    print('______________')
    print(f'Player1: {score_1}')
    print(f'Player2: {score_2}')
    if score_1 > score_2:
        print('\nPlayer1 Wins!\n')
    elif score_1 < score_2:
        print('\nPlayer2 Wins!\n')
    else:
        print('\nIts a tie\n')
main()
