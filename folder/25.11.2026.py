#Nikita babi 
"""
#1. Palk
m = int(input("How much do you make per hour: "))
h = int(input("How much do you work: "))
s = h*m
n = (s*22)/100
n1 = (s*33)/100
print(f"your salary: {n1 + n}")

#Leidke rohelise  kujundi pindala
import math
d = int(input("Enter the Wight: "))
d1 = int(input("Enter the height: "))
sp = d * d1
d = int(input("Enter the Radious: "))
sk = math.pi * (d**2)
print(f"area of ​​a circle: {sk - sp}")

x = int(input("Enter the x: "))
y = int(input("Enter the y: "))
b = int(input("Enter the b: "))
a = int(input("Enter the a: "))
print(f"answer: {(((x-y)/(a+b))**3)**0.25}")


#Valgusfoor

n = int(input("Enter the Color: 1: red \n 2: yellow \n 3:green \n "))
if n>=1 and n<=3:
    if n==1:
        print("Stop")
    elif n==2:
        print("Wait")
    else:
        print("Go")
else:
    Print("1-3")


#Kolmnurk

u = int(input("Enter the gradus angle in degrees: "))
u1 = int(input("Enter the gradus angle in degrees: "))
u2 = int(input("Enter the gradus angle in degrees: "))

if (u + u1 +u2) == 180:
    if u == 90 or u1 == 90 or u2 == 90:
        print("rectangle")
    elif u1 > 90 or u2 > 90 or u > 90:
        print("Blunt triangle")
    else:
        print("acute-angled polygon")
else:
        print("the sum of the angles is 180 degrees")

"""

n = int(input("11» — север, «12» — запад, «13» — юг, «14» — восток"))
n1 = int(input("0 — продолжайте движение, 1 — поверните налево, -1 — поверните направо."))
if n1>=-1 and n1<=1:
    if n>=11 and n<= 14:
        if n == 11:
            if n1 == 0:
                print("Идем на север")
            elif n1 == 1:
                print("Идем на запад")
            elif n1 == -1:
                print("Идем на восток")
        elif n == 12:     
            if n1 == 0:
                print("Идем на запад")
            elif n1 == 1:
                print("Идем на север")
            elif n1 == -1:
                print("Идем на юг")
        elif n == 13: 
            if n1 == 0:
                print("Идем на юг")
            elif n1 == 1:
                print("Идем на восток")
            elif n1 == -1:
                print("Идем на запад")
        elif n == 14:
            if n1 == 0:
                print("Идем на восток")
            elif n1 == 1:
                print("Идем на север")
            elif n1 == -1:
                print("Идем на юг")
    else:
        print("11-14")
else:
    print("-1 - 1")


















