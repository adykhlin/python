#!/usr/local/bin/python3
# coding=utf-8

import random,time

def sticks_amount():
    '''Let's decide the amount of sticks for a game'''
    amount = ' '
    while type(amount) != int:
        print ("With how many sticks do You want to play?")
        amount = input()
        try:
            amount = int(amount)          
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
    if amount > 9 and amount < 43:
        return int(amount)
    else:
        print ("Impossible amount, we will play with the default amount of sticks (20)")
        return 20 

def again():
    '''We just ask a person for another game'''
    global amount
    print("Do you want to play again?")
    if input().lower().startswith('y'):
        amount=sticks_amount()
        goes_first()
    else:
        print ("Thanks for playing")
        print()
        time.sleep(0.5)
        quit()

def game():
    '''Just what we need to grab sticks'''
    global amount
    move = 0
    while move not in [1,2,3]:
        print ("How many sticks do You want to take? (Only 1, 2 or 3)")
        move = input()
        try:
            move = int(move)
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
    amount = amount - move
    if amount <= 0:
        print ("You have lost!")
        #quit()
        again()        
    print ("Left:"+amount*" |", amount)
    pc_move()
    return amount

def pc_move():
    '''Game AI'''
    global amount
    if amount > 1 and amount < 5:
        amount = 1
        print("So, I move")
        print ("Left:"+amount*" |", amount)
    elif amount%4 == 0 and amount > 1:
        amount -= 3
        if amount <= 0:
            print ("I have lost!")
            #quit()
            again()
        print("So, I move")
        print ("Left:"+amount*" |", amount)
    elif (amount-1)%4 == 0:
        amount -= random.randint(1,3)
        if amount <= 0:
            print ("I have lost!")
            #quit()
            again()
        print("So, I move")
        print ("Left:"+amount*" |", amount)
    else:
        small = amount
        small -= 4
        while small > 4:
            small -= 4
        amount -= (small-1)
        if amount <= 0:
            print ("I have lost!")
            #quit()
            again()
        print("So, I move")
        print ("Left:"+amount*" |", amount)
    game()
    return amount
        
def goes_first():
    '''Random decision for the first move'''
    r = random.randint(0,1)
    if r == 0:
        print ("PC goes first")
        pc_move()
    else:
        print ("Player goes first")
        game()
amount=sticks_amount()
print ("Left:"+amount*" |", amount)
goes_first()
