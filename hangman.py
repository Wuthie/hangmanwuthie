import random
print("Welcome to the game of Rock Paper and Scissors")
print("First to three win the game.")
username = input("Please enter your name: ")

#Constants
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
win_msg = '''YOU WON
==========='''
lost_msg = '''YOU LOST
==========='''
draw_msg = '''YOU DRAW
==========='''
choices = ["rock", "paper", "scissors"]
state = 0
user_score_t = 0
bot_score_t = 0

#functions
def bot_choice_func ():
    '''
    bot_choice 1 of 3 choices:
    - rock
    - paper
    - scissors
    return bot_choice
    '''
    bot_choice = random.choice(choices)
    return bot_choice

def user_choice_func ():
    '''
    user_choice is one of 3 choices:
    0 = rock
    1 = paper
    2 = scissors
    return user_choice
    '''
    user_choice = int(input('''Please input a number corresponding to the choice
                          [0 = rock]  [1 = paper]  [2 = scissors]: '''))
    if user_choice > 2:
        print("Please enter a number accordingly.")
        user_choice_func()
    return user_choice

def convert_user_choice (user_choice):
    '''
    convert user choice
    0 -> rock
    1 -> paper
    2 -> scissors
    return user_choice
    '''
    if user_choice == 0:
        user_choice = "rock"
    elif user_choice == 1:
        user_choice = "paper"
    elif user_choice == 2:
        user_choice = "scissors"
    else:
        print("Please enter a number accordingly.")
        convert_user_choice()
    return user_choice

def compare(user_choice, bot_choice):
    '''
    compare:
    rock beats scissors
    scissors beats paper
    paper beats rock
    print msg accordingly
    return state
    '''
    global state
    if user_choice == "rock" and bot_choice == "rock":
        print(draw_msg)
        state = 2
    elif user_choice == "rock" and bot_choice == "scissors":
        print(win_msg)
        state = 1
    elif user_choice == "rock" and bot_choice == "paper":
        print(lost_msg)
        state = 0
    elif user_choice == "paper" and bot_choice == "paper":
        print(draw_msg)
        state = 2
    elif user_choice == "paper" and bot_choice == "rock":
        print(win_msg)
        state = 1
    elif user_choice == "paper" and bot_choice == "scissors":
        print(lost_msg)
        state = 0
    elif user_choice == "scissors" and bot_choice == "scissors":
        print(draw_msg)
        state = 2
    elif user_choice == "scissors" and bot_choice == "paper":
        print(win_msg)
        state = 1
    elif user_choice == "scissors" and bot_choice == "rock":
        print(lost_msg)
        state = 0
    else:
        print("user shouldn't see this, compare function")
    
    return state


def play_again ():
    '''
    if user input y return true
    if no exit while loop
    return again_game
    '''
    again = input("Do you want to play again? [Y/N]: ")
    if again.lower() == "y":
        again_game = True
    elif again.lower() == "n":
        print("Thanks for playing.")
        again_game = False
    else:
        print("Please enter an available answer")
        again_game = False
        play_again()
    return again_game
    
def user_score_tracker (state):
    '''
    score tracker
    state = 1 = win plus 1 for user
    '''
    global user_score_t
    if state == 1:
        user_score_t += 1 
    else:
        pass
    return user_score_t

def bot_score_tracker (state):
    '''
    score tracker
    state = 0 = lost plus 1 for bot
    '''
    global bot_score_t
    if state == 0:
        bot_score_t += 1
    else:
        pass
    return bot_score_t


def scoreboard (user_score, bot_score):
    print(f'''
    ===========================
           SCOREBOARD
    
    {username} : {user_score}
    BOT : {bot_score}
    ''')

def printhand_user (user_choice):
    if user_choice == "rock":
        print(rock)
    elif user_choice == "paper":
        print(paper)
    elif user_choice == "scissors":
        print(scissors)

def printhand_bot (bot_choice):
    if bot_choice == "rock":
        print(rock)
    elif bot_choice == "paper":
        print(paper)
    elif bot_choice == "scissors":
        print(scissors)


def game ():
    user_choice = user_choice_func()
    bot_choice = bot_choice_func()
    converted_choice = convert_user_choice(user_choice)
    state = compare(converted_choice, bot_choice)
    user_score = user_score_tracker(state)
    bot_score = bot_score_tracker(state)
    print("You chose:")
    printhand_user(converted_choice)
    print("The bot chose:")
    printhand_bot(bot_choice)
    scoreboard(user_score, bot_score)

def clearscore():
    global user_score_t
    global bot_score_t
    user_score_t = 0
    bot_score_t = 0

#first to three win
again_game = True
while again_game == True:
    while user_score_t < 3 and bot_score_t < 3:
        game()
        if user_score_t == 3:
            print("CONGRATULATION, YOU WON")
        elif bot_score_t == 3:
            print("SORRY, YOU LOST.")
        elif user_score_t < 3 and bot_score_t <3:
            print("COME ON YOU CAN DO IT!")
        else:
            print("User shouldnt see this, while loop")
    clearscore()
    again_game = play_again()


