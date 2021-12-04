# import random
# attemps_list = []

# def show_score ():
#     if len(attemps_list) <= 0:
#         print('There is no high score yet. Keep playing!')
#     else:
#         print('The current highscore is {}'.format(min(attemps_list)))

# def start_game():
#     random_number = int(random.randint(1, 100))
# print('Hi traveller! Welcome to the game of guesses.')
# name = input('What is your name?')
# play = input('Hi, {}, would you want to play? (Enter Yes/No)'.format(name))

#     attempts = 0
#     show_score()
#     while play.lower() == "yes":
#         try:
#             guess = input("Enter a number between 1 and 100")
#                 if int(guess) < 1 or int(guess) > 100:
#                     raise ValueError("Please enter a number within the given range")
#                 if int(guess) == random_number:
#                     print('Awesome! You guessed right')
#         except ValueError as err:
#             print("Answer not valid, try again.")

""" Number Guessing Game
----------------------------------------
"""
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    
    attempts = 0
    show_score()
    if wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    start_game()
    