"""
a = 29
b = 13
c = 9

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)

arv = int(input())

if arv > 0:
    print("Positive")
elif arv == 0
    print("Neutral")
else:
    print("Neutral")

import math
print("1 - radius R, 2. - diameter D = 2 · R, 3. - length L = 2 · Pi · R, 4. - area S = Pi · R2.")
import math
choice = int(input())
if choice >= 1 and choice <= 4:
    if choice == 1:
        r = int(input("Enter the Radius: "))
        d=2*r
        l=2*math.pi*r
        s=math.pi*r*r
        print(f"R={r} D={d} L={round(l,2)} S={round(s,2)}")
    elif choice == 2:
        d = int(input("Enter the Diameter: "))
        r=d/2
        l=2*math.pi*r
        s=math.pi*r*r
        print(f"R={r} D={d} L={round(l,2)} S={round(s,2)}")
    elif choice == 3:
        l = int(input("Enter the lenght: "))
        r=l/(2*math.pi)
        d=2*r
        s=math/pi*r*r
        print(f"R={r} D={d} L={round(l,2)} S={round(s,2)}")
    elif choice == 4:
        s=int(input("Enter the S: "))
        r=math.sqrt(s/math.pi)
        d=2*r
        l=2*math.pi*r
        print(f"R={r} D={d} L={round(l,2)} S={round(s,2)}")
else:
    print("your number isn't correct")

number = int(input("Enter the number 100-999: "))

if number>=100 and number<=999:
    n = ""
    ntq = ""
    nteq = ""
    nthq = ""
    h = number//100
    nt = number%100//10
    nte = number%100%10
    if h == 1:
        n = "One hundred"
    elif h == 2:
        n = "Two hundred"
    elif h == 3:
        n = "Three hundred"
    elif h == 4:
        n = "Four hundred"
    elif h == 5:
        n = "Five hundred"
    elif h == 6:
        n = "Six hundred"
    elif h == 7:
        n = "Sevem hundred"
    elif h == 8:
        n = "Eight nundred"
    elif h == 9:
        n = "Nine hunred"
        
    if nt == 1:
        ntq = "ten"
    elif nt == 2:
        ntq = "twenty"
    elif nt == 3:
        ntq = "Thirty"
    elif nt == 4:
        ntq = "Forty"
    elif nt == 5:
        ntq = "Fifty"
    elif nt == 6:
        ntq = "Sixty"
    elif nt == 7:
        ntq = "Seventy"
    elif nt == 8:
        ntq = "Eighty"
    elif nt == 9:
        ntq = "Ninety"

    if nte == 1:
        nteq = "One"
    elif nte == 2:
        nteq = "Two"
    elif nte == 3:
        nteq = "Three"
    elif nte == 4:
        nteq = "Four"
    elif nte == 5:
        nteq = "five"
    elif nte == 6:
        nteq = "Six"
    elif nte == 7:
        nteq = "Seven"
    elif nte == 8:
        nteq = "Eight"
    elif nte == 9:
        nteq = "Nine"
        
    if nt == 1 and nte>= 1 and nte<= 9:
        
        if nte == 1:
            nthq = "Eleven"
        elif nte == 2:
            nthq = "Twelve"
        elif nte == 3:
            nthq = "Thirteen"
        elif nte == 4:
            nthq = "Fourteen"
        elif nte == 5:
            nthq = "Fifteen"
        elif nte == 6:
            nthq = "Sixteen"
        elif nte == 7:
            nthq = "Seventeen"
        elif nte == 8:
            nthq = "Eighteen"
        elif nte == 9:
            nthq = "Nineteen"
    if nthq:
        result = f" {n} {nthq}"     
    else:
        result = f" {n} {ntq} {nteq}"
    print(result)
else:
    print("Your number isn't correct")


d = int(input("Enter Day of the month: "))
m = int(input("Enter month of the year: "))

if m==1:
    if d<20:
        print("Capricorn")
    else:
        print("Aquarius")
elif m==2:
    if d<19:
        print("Aquarius")
    else:
        print("Fish")
elif m==3:
    if d<21:
        print("Fish")
    else:
        print("Aries")
elif m==4:
    if d<20:
        print("Aries")
    else:
        print("Taurus")
elif m==5:
    if d<21:
        print("Taurus")
    else:
        print("Twins")
elif m==6:
    if d<22:
        print("Twins")
    else:
        print("Cancer")
elif m==7:
    if d<23:
        print("Cancer")
    else:
        print("Lion")
elif m==8:
    if d<23:
        print("Lion")
    else:
        print("Virgo")
elif m==9:
    if d<23:
        print("Virgo")
    else:
        print("Scales")
elif m==10:
    if d<23:
        print("Scales")
    else:
        print("Scorpion")
elif m==11:
    if d<23:
        print("Scorpion")
    else:
        print("Sagittarius")
elif m==12:
    if d<22:
        print("Sagittarius")
    else:
        print("Capricorn")
        
"""

import random

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
n4 = random.randint(1, 10)
n5 = random.randint(1, 10)
n6 = random.randint(1, 10)
n7 = random.randint(1, 10)
n8 = random.randint(1, 10)
n9 = random.randint(1, 10)
n10= random.randint(1, 10)

answer1 = int(input(f"{n1}*{n2} = "))
answer2 = int(input(f"{n3}*{n4} = "))
answer3 = int(input(f"{n5}*{n6} = "))
answer4 = int(input(f"{n7}*{n8} = "))
answer5 = int(input(f"{n9}*{n10} = "))

a1 = n1*n2
a2 = n3*n4
a3 = n5*n6
a4 = n7*n8
a5 = n9*n10
    
if answer1 == n1*n2:
    print(f"{n1}*{n2} = {a1} Right")
else:
    print(f"{n1}*{n2} = {answer1} not true, answer = {a1}")
        
if answer2 == n3*n4:
    print(f"{n3}*{n4} = {a2} Right")
else:
    print(f"{n3}*{n4} = {answer2} not true, answer = {a2}")
        
if answer3 == n5*n6:
    print(f"{n5}*{n6} = {a3} Right")
else:
    print(f"{n5}*{n6} = {answer3} not true, answer = {a3}")
        
if answer4 == n7*n8:
    print(f"{n7}*{n8} = {a4} Right")
else:
    print(f"{n7}*{n8} = {answer4} not true, answer = {a4}")
        
if answer5 == n9*n10:
    print(f"{n9}*{n10} = {a5} Right")
else:
    print(f"{n9}*{n10} = {answer5} not true, answer = {a5}")




























