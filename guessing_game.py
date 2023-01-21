import random
from statistics import median, mean, mode


def start_game():
    random_num = random.randint(1, 100)
    print('Welcome to the Number Guessing Game')
    guess_count = 0
    guess_list = []
    while True:
        try:
            player_guess = int(input('Guess a number between 1 and 100 inclusive.\n'))

            if player_guess > 100:
                print('Detected that your number is larger than 100. Please choose a lower number.')
            elif player_guess < 1:
                print('Detected that your number is smaller than 1. Please choose a higher number')
            elif player_guess > random_num:
                print("Too High. Try Again.")
                guess_count += 1
            elif player_guess < random_num:
                print("Too low. Try again.")
                guess_count += 1
            else:
                guess_count += 1
                guess_list.append(guess_count)
                print("You Win!")

                # Get Mean, Median, and Mode and print them
                guess_mean = mean(guess_list)
                guess_median = median(guess_list)
                guess_mode = mode(guess_list)

                # Print statistics to screen
                print("Game Stats:")
                print(f"Number of guesses: {guess_count}")
                print(f"Mean of guesses: {guess_mean}")
                print(f"Median of guesses: {guess_median}")
                print(f"Mode of guesses: {guess_mode}")

                play_again_input = input("Would you like to try again? Type [Y] for Yes or [N] for no\n")

                if play_again_input == "Y":
                    print(f'Least Number of Guesses so far is {min(guess_list)}')
                    random_num = random.randint(1, 100)
                    guess_count = 0 # clearing out the guess count for the new game
                    continue
                elif play_again_input == "N":
                    print("Thanks for playing! See you later!")
                    exit()
                else:
                    print('Detected invalid input. Please only enter Y or N.')

        except ValueError:
            print('Detected invalid input. Please only enter numbers.')


# Kick off the program by calling the start_game function.
start_game()
