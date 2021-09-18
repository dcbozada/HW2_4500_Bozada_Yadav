''' Homework 2 9 (Double or Nothing) - Created by Dylan Bozada & Priyanka Yadav
    Program Language: Python :)
    Date: 09/15/2021
    Class: CMP_SCI 4500
    External Files: None
    
    This program is a simulated casino environment were the
    user will be playing a modified verison of the game 'roulette' '''

# Importing necessary packages
import random
import math

# Defining global variables to be accessed by all functions of the program
num_slots, num_slots_zero, num_visits, num_money = 0, 0, 0, 0
visit_wins = []

# Defining funtions for the program

''' This function will begin the program
    It will greet the user, explain that we are about 
    to hit up the casino and play roulette
    
    Here we are going to prompt the user to enter the 
    specifications of their visit; 
    1.) How many slots
    2.) How many slots will have 0 or 00 
    3.) How many times they want to visit the casino
    4.) How much money they would like to start out each visit '''

def welcome():
    # Welcoming the user to the casino 
    welcome_msg = """
        Welcome to the Casino!
        
        Today we are going to be playing the game Roulette."""
    print(welcome_msg)

    input(f'\n\tPress the Enter key to continue...\n')

    # Prompting user for their visit specifications
    visit_details_msg = """
        Before we get started, I will need a couple things from you (four things to be exact):"""
    print(visit_details_msg)

    # Asking for number of slots, how many slots will have 0/00, number of visits, and amount of money
    global num_slots, num_slots_zero, num_visits, num_money

    num_slots = int(input(f'\n\t1.) How many slots will be in your roulette wheel? Choose a number between 2 and 200: '))
    # Input check
    while num_slots < 2 or num_slots > 200:
        print(f'\tThat was not a valid input...')
        num_slots = int(input(f'\n\t1.) How many slots will be in your roulette wheel? Choose a number between 2 and 200: '))

    num_slots_zero = int(input(f'\t2.) How many of the slots will be labeled with 0 or 00? Choose a number between 0 and 2: '))
    # Input check
    while num_slots_zero < 0 or num_slots_zero > 2:
        print(f'\tThat was not a valid input...')
        num_slots_zero = int(input(f'\t2.) How many of the slots will be labeled with 0 or 00? Choose a number between 0 and 2: '))

    num_visits = int(input(f'\t3.) How many times do you want to visit the casino? Choose a number between 1 and 100,000: '))
    # Input check 
    while num_visits < 1 or num_visits > 100_000:
        print(f'\tThat was not a valid input...')
        num_visits = int(input(f'\t3.) How many times do you want to visit the casino? Choose a number between 1 and 100,000: '))

    num_money = int(input(f'\t4.) How much money do you want to start with? Choose a number between 1 and 1,000,000: '))
    # Input check
    while num_money < 1 or num_money > 1_000_000:
        print(f'\tThat was not a valid input...')
        num_money = int(input(f'\t4.) How much money do you want to start with? Choose a number between 1 and 1,000,000: '))

def bet_choice():
    # Giving the user their betting options
    bet_msg = """

        Alright, now we are going to choose a betting strategy. You have three choices... 

        1.) The Martingale strategy, you will start by betting $1. If you win your bet, you quit. If you lose, you double the bet and go again. 
            (This process will continue until you are either out of money, or you win and would like to leave the casino)
            
        2.) A random strategy, each time you bet, you bet a random amount from $1 to all of the money you have left.
            (This strategy will continue until you either run out of money, or you have bet 50 times, whichever comes first)
        
        3.) A fixed bet strategy, each time you bet, you bet a fixed amount, from $1 to the amount of money you start with.
            (This strategy will continue until you either run out of money (*the amount of money left dips below the fixed bet size) or you have bet 50 times)"""
    print(bet_msg)

    user_choice = int(input(f'\n\tEnter 1, 2 , or 3 to choose your strategy: '))
    if user_choice == 1:
            martingale()
    elif user_choice == 2:
            rndm()
    elif user_choice == 3:
            fixed()

    # Input check
    while user_choice < 1 or user_choice > 3:
        print(f'\n\tThat was not a valid input...')
        user_choice = int(input(f'\n\tEnter 1, 2 , or 3 to choose your strategy: '))
        if user_choice == 1:
            martingale()
        elif user_choice == 2:
            rndm()
        elif user_choice == 3:
            fixed()

# This function will spin the wheel and return the user's color they landed on 
def wheel_spin():
    global num_slots, num_slots_zero
    # Total slots on wheel including zeroes
    if num_slots_zero == 0:
        total_slots = num_slots
    elif num_slots_zero == 1:
        total_slots = (num_slots - 1) + num_slots_zero
    elif num_slots_zero == 2:
        total_slots = (num_slots - 2) + num_slots_zero

    # Strings to assign number to color
    black, red, green, user_color = 'black', 'red', 'green', ''

    # Creating list of numbers, we have to do this to makeup for the fact that there may or may not be zeroes in the wheel
    # We will also replace 1 or 2 of the numbers in the list with 0 if the user selected to have zeroes on the wheel
    slot_list = []
    for i in range(1, total_slots + 1):
        slot_list.append(i)

    if num_slots_zero == 1:
        slot_list[random.randrange(total_slots)] = 0
    elif num_slots_zero == 2:
        slot_list[random.randrange(total_slots)] = 0
        slot_list[random.randrange(total_slots - 1)] = 0

    # Generating random number, and modulus to determine if wheel landed on black or red
    # Even = black, Odd = red, 0 = green
    num_landed = random.choice(slot_list)
    if num_landed % 2 == 0:
        user_color = black
    elif num_landed % 2 != 0:
        user_color = red
    elif num_landed == 0:
        user_color = green

    return(user_color)

def martingale():
    global num_visits, num_money, visit_wins

    print(f'\n\tMartingale!')
    print(f'\n\tGoing to the casino...')

    for visits in range(num_visits):
        # Starting bet of $1, and creating wallet equal to user input of money they started with 
        bet = 1
        wallet = num_money

        while wallet > 0:
            wallet -= bet
            color = wheel_spin()
            if color == 'black':
                wallet += (bet*2)
                break
            elif color == 'red':
                bet *= 2
                continue
            elif color == 'green':
                wallet += bet
                continue

        visit_wins.append(wallet)

def rndm():
    global num_visits, num_money, visit_wins
    print(f'\n\tRandom!')
    print(f'\n\tGoing to the casino...')

    for visits in range(num_visits):
        # Starting bet, random number between 1 and amount of money
        bet = random.randrange(1, num_money)
        bet_limit = 0
        wallet = num_money

        while wallet >= bet and bet_limit < 50:
            wallet -= bet
            color = wheel_spin()
            if color == 'black':
                wallet += (bet*2)
                bet_limit += 1
                continue
            elif color == 'red':
                bet_limit += 1
                continue
            elif color == 'green':
                wallet += bet
                bet_limit += 1
                continue

        visit_wins.append(wallet)

def fixed(): 
    global num_visits, num_money, visit_wins

    print(f'\n\tFixed!')
    bet = int(input(f'\tPlease choose a number between 1 and ' + str(num_money) + ': '))
    if bet < 1 or bet > num_money:
        print(f'\n\tNot an option...')
        bet = int(input(f'\tPlease choose a number between 1 and ' + str(num_money) + ': '))

    print(f'\n\tGoing to the casino...')

    for visits in range(num_visits):
        # Starting bet, random number between 1 and amount of money
        bet_limit = 0
        wallet = num_money

        while wallet >= bet and bet_limit < 50:
            wallet -= bet
            color = wheel_spin()
            if color == 'black':
                wallet += (bet*2)
                bet_limit += 1
                continue
            elif color == 'red':
                bet_limit += 1
                continue
            elif color == 'green':
                wallet += bet
                bet_limit += 1
                continue

        visit_wins.append(wallet)

# Summary of casino visits
def summary():
    global num_money, num_slots, num_slots_zero, num_visits, visit_wins
    start_summary = """
        Alrighty, just wrapped up. Here is a summary of your casino visits!

        """
    print(start_summary)

    # Telling user the initial inputs
    print(f'\tHere are your initial inputs:\n')
    print(f'\tAmount of slots on the wheel:', num_slots)
    print(f'\tAmount of slots with zero on the wheel:', num_slots_zero)
    print(f'\tAmount of visits to the casino:', num_visits)
    print(f'\tAmount of money you started each visit with:', num_money)

    # Telling user the total number of dollars they put at risk
    total_risk = num_visits * num_money
    print(f'\n\tThis is the total amount of money you risked in all of your visits:', total_risk)

    # Telling user the total amount they walked away with
    total_walked_away = 0
    for i in range(len(visit_wins)):
        total_walked_away += visit_wins[i]
    print(f'\n\tThe total amount of money you walked away with:', total_walked_away)
    
    # Telling use their best gain at a visit
    best_visit = max(visit_wins)
    if best_visit > num_money:
        best_gain = best_visit - num_money
        print(f'\n\tYour best gain was:', best_gain)
    elif best_visit < num_money:
        print(f'\n\tYou did not walk away a winner in any of your visits :(')

    # Telling how many visits ended with zero money left
    visit_no_money = 0
    for i in range(len(visit_wins)):
        if visit_wins[i] == 0:
            visit_no_money += 1

    if visit_no_money > 0:
        print(f'\n\tYou had', str(visit_no_money), ' visits that you left with zero dollars')
    elif visit_no_money == 0:
        print('f\n\tYou left with some money each visit! Nice!')
        
    # Computing average of money change in N visits, then letting user know
    top_of_change = 0

    for i in range(0, (len(visit_wins) - 1)):
        num_between = (visit_wins[i] + visit_wins[i + 1]) / 2
        dist_between = (visit_wins[i] - num_between) * 2
        top_of_change += dist_between

    bottom_of_change = num_visits - 1

    average_of_change = top_of_change / bottom_of_change

    print(f'\n\tThe average change of your money in the visits:', math.ceil(average_of_change))

    # Telling user how many times through their visits they were a winner, loser, and broke even
    total_wins = 0
    total_loss = 0
    total_broke_even = 0

    for i in range(len(visit_wins)):
        if visit_wins[i] > num_money:
            total_wins += 1
        elif visit_wins[i] > num_money:
            total_loss += 1
        elif visit_wins[i] > num_money:
            total_broke_even += 1

    print(f'\n\tYou had', total_wins, 'visits you left a winner')
    print(f'\n\tYou had', total_loss, 'visits you left a loser')
    print(f'\n\tYou had', total_broke_even, 'visits you left and broke even')

welcome()
bet_choice()
summary()

print(f'\n\n\tThanks for playing! Have a good one!\n')
