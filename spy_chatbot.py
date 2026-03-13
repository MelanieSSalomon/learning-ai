# Spy Themed Chatbot
# Practice project for learning lpoops, functions, and user input
# Buikt during AI software engineering coursework

import sys
import random
import time

def type_text(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
print()        

def random_spy_name():
    spy_names = ["Agent Phoenix", "Agent Shadow", "Agent Cobra", "Agent Thunder", "Agent Eclipse"]
    name = random.choice(spy_names)
    print("Welcome,", name)
    return name

def dramatic_intro():
    print("Accessing global surveillance grid…")
    time.sleep(1.2)
    print ("Initializing classified operation…")
    time.sleep(1.2)
    print("Encrypting transmissions. Awaiting agent authentication.")
    time.sleep(1.2)
    print("Warning: Intruders detected in Sector 7.")
    time.sleep(1.2)
    print("The fate of the world rests on your next move…")
    time.sleep(1.2)

def get_kevin_hart_phrases():
    phrases = [ "I'm not gonna tell you again!",
        "Pineapples! It's the safe word!",
        "You gon' learn today!",
        "That's a sign of war!",
        "Say it with your chest, little man!" ]

    return random.choice(phrases)   

dramatic_intro()
random_spy_name()

user_name = input("Agent, identify yourself: ")
print (f"Welcome, Agent {user_name}! Reason for your visit?")

while True:
    user_input = input("Type something: ")
    print("Debug:", user_input)

    if user_input.lower() == "quit":
        print("Mission terminated. Signing off!")
        break

    bot_reply = get_kevin_hart_phrases() + " " + user_input
    type_text("Bot: " + bot_reply)


    
    
