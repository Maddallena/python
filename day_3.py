#DZIEŃ TRZECI ____________________________________________________________________________________________________________________

#przykład pierwszy, if, elif, else

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         bill = 5
#         print(f"Child tickets are ${bill}.")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth tickets are ${bill}.")
#     elif age >= 45 & age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print(f"Adult tickets are ${bill}.")
    
#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry, you have to grow taller before you can ride.")

#zadanie1 Odd or Even

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#zadanie2  BMI calculator.2
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly obese.")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")
    

#zadanie3 leap year
# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not a leap year.")
#     else:
#         print("Leap year.")        
# else:
#    print("Not a leap year.")

#zadanie4 pizza

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
    
# if extra_cheese == "Y":
#     bill += 1
    
# print(f"Your final bill is ${bill}.")


#zadanie5 Love calculator

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# both = (name1 + name2).lower()

# true = both.count("t") + both.count("r") + both.count("u") + both.count("e")
# love = both.count("l") + both.count("o") + both.count("v") + both.count("e") 
# true_love = int(str(true) +str(love))

# if (true_love < 10) or (true_love > 90):
#     print(f"Your score is {true_love}, you go together like coke and mentos.")
# elif (true_love > 40) and (true_love < 50):
#     print(f"Your score is {true_love}, you are alright together.")
# else:
#     print(f"Your score is {true_love}.")


#zadanie6 Treasure Island
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# go = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()

# if go == "left":
#     lake = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower() ####jak zrobić cudzysłów w środku!!!!
#     if lake == "wait":
#         door = input("You arrive at the island unharmed. There is a hose with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
#         if door == "yellow":
#             print("You win!")
#         elif door == "red":
#             print("You're burned by fire. Game Over.")
#         elif door == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#          print("You've been attacked by trout. Game Over.")
# else:
#     print("You've fallen into a hole. Game Over.")  