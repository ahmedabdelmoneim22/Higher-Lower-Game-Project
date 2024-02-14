#Divide and conquer algorithms.
#Divide-and-conquer.
#******************.
#1)Divide the problem into a number
#of subproblems that are smaller instances of the same problem.
#2)Conquer the subproblems by solving them recursively.
#If they are small enough, solve the subproblems as base cases.
#3)Combine the solutions to the subproblems into
#the solution for the original problem.
#******************.
from art import logo,vs
from  game_data import data
import random
#"Don't repeat yourself" (DRY).
def format_data(account):
    """"Format the account data into printable format."""
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
def check_answer(guess,a_followers,b_followers):
    """Use if statement to check if user is correct."""
    """Take the user guess and follower counts and returns if they got it right."""
    """Skitch-Apple-->>Skitch."""
    """     GuessA      GuessB"""
    """A>B  True        False"""
    """B>A  False       True"""
    if a_followers > b_followers:
        return guess == "a" # Check  if guess== "a" if True return True.
    else:
        return guess == "b" # Check if guess== "b" if True return True.
# Display-art.
print(logo)
score=0
game_should_continue = True
account_b=random.choice(data)
# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data.
    # Making account at position B become the next account at position A.
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    # Ask user for guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    # Give user feedback on their Guess.
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue=False
        print(f"Sorry, that's wrong. Final score: {score}.")
########################################
########################################
########################################

