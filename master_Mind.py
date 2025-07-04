#!/bin/python3
# MasterMind
# by ICTROCN
# v1.03
# 15-8-2024
# Last mod by ChatGPT : added user story 2 - improved input validation and error messages

import random

def generate_Code(length=4, digits=6):
    """
    Genereert een willekeurige geheime code.
    
    Args:
        length (int): Lengte van de code.
        digits (int): Maximaal cijfer (1 tot digits).
    
    Returns:
        list: Lijst met string cijfers als code.
    """
    return [str(random.randint(1, digits)) for _ in range(length)]

def is_valid_guess(guess, length=4, digits="123456"):
    """
    Controleert of de gok geldig is.
    Geeft True terug als guess 4 cijfers lang is en alleen cijfers uit digits bevat.
    """
    return len(guess) == length and all(c in digits for c in guess)

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        while True:
            guess = input(f"Attempt {attempt}: ").strip()
            
            if guess == "cheat":
                show_Secret(secret_Code)
                continue
            
            if not is_valid_guess(guess):
                print("Invalid input! Please enter exactly 4 digits, each between 1 and 6.")
            else:
                break

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    # User Story 1 test: print some generated codes to check randomness
    print("Test: Generated codes for User Story 1")
    for _ in range(3):
        print(generate_Code())

    again = 'Y'
    while again == 'Y':
        play_Mastermind()
        again = input("Play again (Y/N)? ").upper()
