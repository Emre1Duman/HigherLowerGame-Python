#Breakdown the todo list into comments
import random,  art
from game_data import data

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
    dct.clear()
    dct.update(b)

# def update_details(dict):
#     global name
#     name = dict["name"]
#     # description = dict["description"]
#     # country = dict["country"]
#     # followers = dict["follower_count"]

endgame = False
while not endgame:

    print(f"Compare A: {name_a}, {description_a}, from {country_a}, answer = {followers_a}")
    print(f"Compare B: {name_b}, {description_b}, from {country_b}, answer = {followers_b}")
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    if guess == "a":
        if followers_a > followers_b:
            score += 1
            replace_a(a)
            name_a = a["name"]
            description_a = a["description"]
            country_a = a["country"]
            followers_a = a["follower_count"]
            b = random.choice(data)
            name_b = b["name"]
            description_b = b["description"]
            country_b = b["country"]
            followers_b = b["follower_count"]
            print(f"You're right! Current score: {score}")
        else:
            #Clear screen & end loop
            print(f"Sorry, that's wrong. Finale score: {score}")
            endgame = True
    elif guess == "b":
        if followers_b > followers_a:
            score += 1
            replace_a(a)
            name_a = a["name"]
            description_a = a["description"]
            country_a = a["country"]
            followers_a = a["follower_count"]
            b = random.choice(data)
            name_b = b["name"]
            description_b = b["description"]
            country_b = b["country"]
            followers_b = b["follower_count"]
            print(f"You're right! Current score: {score}")
        else:
            #Clear screen & end loop
            print(f"Sorry, that's wrong. Finale score: {score}")
            endgame = True







