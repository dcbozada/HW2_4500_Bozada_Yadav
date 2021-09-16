''' Homework 2 9 (Double or Nothing) - Created by Dylan Bozada & Priyanka Yadav
    Date: 09/15/2021
    Class: CMP_SCI 4500
    External Files: None
    
    This program is a simulated casino environment were the
    user will be playing a modified verison of the game 'roulette' '''

# Defining global variables to be accessed by all functions of the program
num_slots, num_slots_zero, num_visits, num_money = 0, 0, 0, 0

# Debugging 
print(f'\n\t\t num vars before welcome', num_slots, num_slots_zero, num_visits, num_money)

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

    input(f'\n\tPress any key to continue...\n')

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
    # Input c heck 
    while num_visits < 1 or num_visits > 100_000:
        print(f'\tThat was not a valid input...')
        num_visits = int(input(f'\t3.) How many times do you want to visit the casino? Choose a number between 1 and 100,000: '))

    num_money = int(input(f'\t4.) How much money do you want to start with? Choose a number between 1 and 1,000,000: '))
    # Input check
    while num_money < 1 or num_money > 1_000_000:
        print(f'\tThat was not a valid input...')
        num_money = int(input(f'\t4.) How much money do you want to start with? Choose a number between 1 and 1,000,000: '))

def bet_choice():
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
    while user_choice < 1 or user_choice > 3:
        print(f'\n\tThat was not a valid input...')
        user_choice = int(input(f'\n\tEnter 1, 2 , or 3 to choose your strategy: '))

        if user_choice == 1:
            martingale()
        elif user_choice == 2:
            random()
        elif user_choice == 3:
            fixed()

def martingale():
    print(f'\n\tmartingale')

def random():
    print(f'\n\trandom')

def fixed(): 
    print(f'\n\tfixed')

welcome()
bet_choice()

