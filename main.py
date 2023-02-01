from art import logo, vs
from game_data import data
import random
# limpar o console
import os
clear = lambda: os.system('cls')
# limpar o console

score = 0

account_b = random.choice(data)

while(score >= 0):
    clear()
    print(logo)
    random.choice(data)

    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    def format_data(account):
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f"{account_name}, a/an {account_description}, from {account_country}"

    def check_answer(guess, a_followers, b_followers, score):
        winner = ""
        if a_followers > b_followers:
            winner = "a"
        else:
            winner = "b"
        if(guess != winner):
            print("XXXXXXXXXXXXXXXXXXXXXX")
            print(f"X     You Lose !!    X\n" + 
                    f"X   Final Score: {score}   X")
            print("XXXXXXXXXXXXXXXXXXXXXX")

            return -1
        else:
            score += 1
            print("\n=================================================================\n")
            print(f"\nYou Win !! Your current score: {score} :D")
            print("\n=================================================================\n")
        return score


    print(f"Compare A: {format_data(account_a)},\n{vs}\nAgainst B: {format_data(account_b)};")
    print("-------------------------------------------------------------")
    guess = input("Who has more followers? Type 'A' or 'B':  ").lower()
    print("-------------------------------------------------------------")

    score = check_answer(guess, account_a["follower_count"], account_b["follower_count"], score)
