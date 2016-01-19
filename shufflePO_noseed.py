#!/usr/local/bin/python3
import random
import os
l = []
try: gr_c = int(input("How many teams participating? "))
except ValueError: print("Not a digit, please try again"); exit()
while gr_c < 2 or gr_c % 2 != 0: 
    print("Wrong amount of teams");
    gr_c = int(input("How many teams participating? "))
for i in range (1, gr_c+1):
    inp = input ("Input %i team: " % (i))
    while inp=="": print("Blank input, try again?"); inp = input("Input %i team: " % (i))
    if inp != '': l.append(inp)
    random.shuffle (l)
print()
while l:
    pop1 = l.pop(); pop2 = l.pop()
    random.shuffle (l)
    print(str(pop1) + " - " + str(pop2))
print()
input("Press <Enter> to exit the app\n")
