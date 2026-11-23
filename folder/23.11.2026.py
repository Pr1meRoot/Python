"""
n = int(input("Enter the number 1-10: "))
n1 = int(input("Enter the number 1-10: "))
if n1>n:
    print("Second number is more")
elif n1<n:
    print("first number is more")
else:
    print("The numbers are the same")

n2 = int(input("Enter the number 1-10: "))
n3 = int(input("Enter the number 1-10: "))
n4 = int(input("Enter the number 1-10: "))

if n2<n3 and n2<n4:
    print(n2)
elif n3<n2 and n3<n4:
    print(n3)
else:
    print(n4)


a = int(input("Enter the number 1-10: "))
b = int(input("Enter the number 1-10: "))
c = int(input("Enter the number 1-10: "))

if a==b==c:
    print("3")
elif a==b or b==c or a==c:
    print("2")
else:
    print("1")


s = int(input("The column of the first cell: "))
k = int(input("The row of the first cell: "))
s1 = int(input("The column of the first cell: "))
k2 = int(input("The row of the first cell: "))

if ((s+k)%2)== 0:
    q = 2
elif ((s+k)%2)== 1:
    q = 1
if ((s1+k2)%2)== 0:
    qq = 2
elif ((s1+k2)%2)== 1:
    qq = 1
if q == 2 and qq ==2:
    print("colors are the same")
elif q == 1 and qq == 1:
    print("colors are the same")
else:
    print("colors aren't the same")


y = int(input("The column of the first cell: "))
x = int(input("The row of the first cell: "))
y1 = int(input("The column of the first cell: "))
x1 = int(input("The row of the first cell: "))

if y == y1 or x == x1:
    print("yes")
else:
    print("no")


y = int(input("The column of the first cell: "))
x = int(input("The row of the first cell: "))
y1 = int(input("The column of the first cell: "))
x1 = int(input("The row of the first cell: "))

if y == y1 and x == x1 or (y+1)==y1 and x1==x or (y-1)==y1 and x1==x or (x-1)==x1 and y==y1 or (x+1)==x1 and y==y1:
    print("yes")
elif (y+1)==y1 and (x-1)==x1 or (x+1)==x1 and (y+1)==y1 or (x+1)==x1 and (y-1)==y1 or (x-1)==x1 and (y-1)==y1:
    print("yes")
else:
    print("no")


y = int(input("The column of the first cell: "))
x = int(input("The row of the first cell: "))
y1 = int(input("The column of the first cell: "))
x1 = int(input("The row of the first cell: "))

if  abs(y-y1)==abs(x-x1):
    print("yes")
else:
    print("no")

y = int(input("The column of the first cell: "))
x = int(input("The row of the first cell: "))
y1 = int(input("The column of the first cell: "))
x1 = int(input("The row of the first cell: "))

if (y+2) == y1 and (x+1) == x1 or (y+1) == y1 and (x+2) == x1 or (y-1) == y1 and (x+2) == x1 or (y-2) == y1 and (x+1) == x1 or (y-2) == y1 and (x+1) == x1 or (y-1) == y1 and (x-2) == x1 or (y+1) == y1 and (x-2) == x1 or (y+2) == y1 and (x-1) == x1 or (x-1)==x1 and (y-2)==y1:
    print("yes")
else:
    print("no")
"""

y = int(input("The column of the first cell: ")) #6
x = int(input("The row of the first cell: ")) #4
k = int(input(": "))

if k%x == 0 or k%y == 0:
    print("yes")
else:
    print("no")






