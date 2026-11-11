
number = int(input("enter a number: "))
print(f"next number {number + 1}")
print(f"The previous number {number - 1}")

length = float(input("what is the distance(M): "))
time = float(input("How much time(sec): "))

distanceKM = length / 1000
timehours = time/3600
speed = distanceKM/timehours
print(f"Speed: {speed} km/h")

TF = float(input("Enter temperature: "))
TK = round((TF+459.67)/1.8 , 2)
print("temperature in kelvins: ", TK) 

School = int(input("how many children: "))
apple = int(input(" how many apples: "))
answer = apple//School
print(f"how much each person should receive {answer}")
print(f"how much will remain in the basket {apple%School}")


class1 = int(input("how many students in the 1 class? "))
class2 = int(input("how many students in the 2 class? "))
class3 = int(input("how many students in the 3 class? "))

desks1 = class1 // 2 + class1 % 2
desks2 = class2 // 2 + class2 % 2
desks3 = class3 // 2 + class3 % 2
desksall = desks1 + desks2 + desks3
print(f" school will needs {desksall} desks")

###
times = int(input("how many minutes have passed: "))

hours = (times // 60) % 24

minutes = times % 60

print(f"right now {hours}:{minutes}") # used ai for help
###

number =  int(input("Enter the number: "))
number1 = number//10
number2 = number % 10

print(f"number of integers: {number1}")
print(f"number of decimal places: {number2}")
