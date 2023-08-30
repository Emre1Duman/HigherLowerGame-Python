#Breakdown the todo list into comments
import random,  art, os
from game_data import data
cls = lambda: os.system('clear')

#Selecting random account, displaying details to set up game
score = 0
a = {}
a = random.choice(data)

name_a = a["name"]
description_a = a["description"]
country_a = a["country"]
followers_a = a["follower_count"]

b = {}
b = random.choice(data)

name_b = b["name"]
description_b = b["description"]
country_b = b["country"]
followers_b = b["follower_count"]

def replace_a(dct):
    """Replace the content of dictionary A, with B"""
    dct.clear()
    dct.update(b)

def update_a(a, b):
    """Update the variables with the new data"""
    global name_a
    global description_a
    global country_a
    global followers_a
    name_a = a["name"]
    description_a = a["description"]
    country_a = a["country"]
    followers_a = a["follower_count"]
    global name_b
    global description_b
    global country_b
    global followers_b
    name_b = b["name"]
    description_b = b["description"]
    country_b = b["country"]
    followers_b = b["follower_count"]


endgame = False
while not endgame:

    if a == b:
        b = random.choice(data)
        name_b = b["name"]
        description_b = b["description"]
        country_b = b["country"]
        followers_b = b["follower_count"]
    else:
        print(art.logo)
        print(f"Compare A: {name_a}, {description_a}, from {country_a}, answer = {followers_a}")
        print(art.vs)
        print(f"Compare B: {name_b}, {description_b}, from {country_b}, answer = {followers_b}")
        guess = input("Who has more followers? Type 'A' or 'B' ").lower()
        if guess == "a":
            if followers_a > followers_b:
                score += 1
                replace_a(a)
                b = random.choice(data)
                update_a(a,b)
                cls()
                print(f"You're right! Current score: {score}")
            else:
                cls()
                print(f"Sorry, that's wrong. Finale score: {score}")
                endgame = True
        elif guess == "b":
            if followers_b > followers_a:
                score += 1
                replace_a(a)
                b = random.choice(data)
                update_a(a,b)
                cls()
                print(f"You're right! Current score: {score}")
            else:
                cls()
                print(f"Sorry, that's wrong. Finale score: {score}")
                endgame = True