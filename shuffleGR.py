#!/usr/local/bin/python3
# coding=utf-8
import random
potA = []
potB = []
potC = []
potD = []
s = 0
l = [potA,potB,potC,potD]
gr_c = input ("What is the amount of groups? ")
try: gr_c = int(gr_c)
except ValueError: print("Not a digit, try again"); exit()
while gr_c < 2: 
    print("Wrong amount of groups");
    gr_c = int(input ("What is the amount of groups? "))
for item in l:
    s += 1
    for i in range (gr_c):
        inp = input ("Input %i team for the %i pot: " % (i+1,s))
        while inp=="": print("Blank input! Try again, please?"); inp = input ("Input %i team for the %i pot: " % (i+1,s))
        if inp != '': item.append(inp)
    random.shuffle (potA); random.shuffle (potB); random.shuffle (potC); random.shuffle (potD)
while potD:
    for counter in range (gr_c):
        pop_a = potA.pop(); random.shuffle (potA)
        pop_b = potB.pop(); random.shuffle (potB)
        pop_c = potC.pop(); random.shuffle (potC)
        pop_d = potD.pop(); random.shuffle (potD)
        print("Group", str(counter) + ":", str(pop_a), str(pop_b), str(pop_c), str(pop_d))
        print("")
input("Press <Enter> to exit the app\n")
