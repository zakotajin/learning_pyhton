# random library for compurter's choices
import random

# getting choices from player and computer
def getchoices():
    p_choice = input("please Enter your choice (rock, paper, scissors):")
    options = ['rock','paper','scissors']
    c_choice = random.choice(options)
    choices = {'player':p_choice, 'computer':c_choice}
    return choices

# checking the winner
def checkwin(player, computer):
    print(f'You chose {player} computer chose {computer}!')
    if player == computer:
        print ('its a tie :|')
    elif player == 'rock':
        if computer == 'paper':
            return 'paper covers rock! you lose!'
        else:
            return 'rock smashes scissors! You won!'
    elif player == 'paper':
        if computer == 'scissors':
            return 'scissors cut paper! you lose!'
        else:
            return 'paper covers rock! You won!'
    elif player == 'scissors':
        if computer == 'paper':
            return 'scissors cuts paper! you won!'
        else:
            return 'rock smashes scissors! you lose!'
    else:
        return 'input not valid! please re run the program and enter a valid choice'


# calling funtions
a = getchoices()
print(checkwin(a['player'], a['computer']))