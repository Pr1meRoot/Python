
a = 3
b = 7
print(a>b)
print(a<b)

print(a>0 and b>0)
print(a>0 and b==5)
print(a!=3 and b>=7)
print(a<0 and b<0)

print(a>0 or b>0)
print(a>0 or b==5)
print(a!=3 or b>=7)
print(a<0 or b<0)

print(a>5 and b<10 or b>20)
print(a>5 and (b<10 or b>20))

x = 6
y = 10
print(x==6 and x<=10) #True
print(x>=7 and y>12) #False

print(x==6 or x<=10) #True
print(x>=7 or y>12) #False

word = input("random word")
print(len(word)> 3 and b==7)

print(a**b==y^5 and b>=x or y+x==b-4)

print(x*y!=0 and y>x)

arv=int(input("Enter the number"))

if arv>=0:
    print("This is a positive number")
elif arv<0:
    print ("This is a negative number")
elif arv==0:
    print("number is 0")
else:
    print("this isn't a number")


if arv%2==0:
    print("this is an even number")
else:
    print("this is an odd number")

dw=int(input("day of the week: "))

if dw==1:
    print("Monday")
elif dw==2:
    print("Tuesday")
elif dw==3:
    print("Wednesday")
elif dw==4:
    print("Thursday")
elif dw==5:
    print("Friday")
elif dw==6:
    print("Saturday")
elif dw==7:
    print("Sunday")
else:
    print("Enter the number 1-7")


if dw>=1 and dw<7:
    print("this is a day of the week")
else:
    print("this is a random number")

month = int(input("Enter the number month: "))
                  
if month>0 and month<12:
    if month==1 or month==2 or month==12:
        print("winter")
    elif month==3 or month==4 or month==5:
        print("Spring")
    elif month==6 or month==7 or month==8:
        print("Summer")
    elif month==9 or month==10 or month==11:
        print("Autumn")
else:
    print("1-12")


km = float(input("Enter the distanced in km: "))
ft = float(input("Entet the distanced in ft: "))

if (km * 1000) > (ft*0.3048):
    print("more kilometers")
elif km * 1000) > (ft*0.3048):
    print("more FT")
else:
    print("they are equal")


password = "cow12345"
pd = str(input("Enter the password: ")).strip()

if pd==password:
    print("password is correct")
else:
    print("password isn't correct")

number = int(input("Enter the two-digit number: "))
a, b = divmod(number, 10)

        if a>b:
        print("the first number is greater")
        elif a<b:
        print("the second number is greateh")
        else:
        print("Error")
    if a+b>=10:
        print("ambiguous number")
    else:
        print("Single digit number")
number = str(number)
if number.find("3")>=0:
    print("The number 3 was found")
else:
    print("THe number 3 was not found")


tk= input("Enter the code")
if (int(tk[0])+int(tk[1])+int(tk[2])) == (int(tk[3])+int(tk[4])+int(tk[5])):
    print("you are win")
else:
    print("you could have won")


grade = int(input("Enter your the grade: "))

if grade>=1 and grade<=5:
    if grade==1:
        print("badly")
    elif grade==2:
        print("not satisfactory")
    elif grade==3:
        print("satisfactory")
    elif grade==4:
        print("Good")
    elif grade==5:
        print("Great")
else:
    print("1-5")

n = int(input("Enter the number: "))
ntwo = int(input("Enter the number: "))
ac = int(input("1 = Addition\n 2 = Subtraction\n 3 = Multiplication\n 4 = Division\n")) #arithmetic choice

if ac==1:
    print(f"answer: {n + ntwo}")
elif ac==2:
    print(f"answer: {n - ntwo}")
elif ac==3:
    print(f"answer: {n * ntwo}")
elif ac==4 and n!=0 and ntwo!=0:
    print(f"answer: {n / ntwo}")


         










