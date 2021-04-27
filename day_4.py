#DZIEŃ CZWARTY _____________________________________________________________________________________________________________________________________

#Random module
# import random

# random_integer = random.randint(1, 10) #random dający liczbę od 1 - 10
# print(random_integer)

# random_float = random.random() * 5 #liczba float w granicy od 0 ale mniejsza od 1, razy 5, to wyjdzie nam miejsza od 5
# print(random_float)

# #how to create a random decimal number between 0 and 5
# random_decimal = random.uniform(1, 5) #w kursie pomnożyła *5, ale ten sposób znalazłam w internecie i służy do randomowych floatów w moich podanych granicach
# print(random_decimal)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

#zadanie1 Heads or tails
# import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# heads_tails = random.randint(0,1)
# if heads_tails == 1:
#     print("Heads")
# else:
#     print("Tails")

# #LISTY!!!
# states_of_america = ["Delaware", "Huston", "Alaska"] #tworzenie listy
# states_of_america[1]
# states_of_america[-1] #podaje pierwsze od końca, ogółem od końca numeruje od 1
# states_of_america[2] = "AlaSka" #zmienia dane w liście na dany indeksie
# states_of_america.append("Magdalenaland") #rozszerza liste o jeden element
# states_of_america.extend(["California", "New York"]) #wydłuża liste o podane elementy

#zadanie2 Who's paying
# import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
# names = namesAsCSV.split(", ")
# print(names)

# names_lenght = len(names)

# random_name = random.randint(0, names_lenght - 1) #żeby nie było więcej niż ma długość tablica, a 0 już przecież mamy
# name_pay = names[random_name]
# print(name_pay + " is going to buy a meal today.")

#nested list
#dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])

#Zadanie3 treasure map
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# where_x = int(position[0])
# where_y = int(position[1])
# if where_x == 1:
#     if where_y == 1:
#         map[0][0] = " x"
#     elif where_y == 2:
#         map[1][0] = " x"
#     else:
#         map[2][0] = " x"
# if where_x == 2:
#     if where_y == 1:
#         map[0][1] = " x"
#     elif where_y == 2:
#         map[1][1] = " x"
#     else:
#         map[2][1] = " x"
# if where_x == 3:
#     if where_y == 1:
#         map[0][2] = " x"
#     elif where_y == 2:
#         map[1][2] = " x"
#     else:
#         map[2][2] = " x"

# #rozwiazanie:
# # selected_row = map[where_y - 1]
# # selected_row[where_x - 1] = "X"
# map[where_y - 1][where_x - 1]="X"
# print(f"{row1}\n{row2}\n{row3}")

#Zadanie rock-paper-scissors
# import random 

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# possibilities = [rock, paper, scissors]
# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# print(possibilities[choice])

# print("Computer chose: ")

# computer = random.randint(0, 2)
# print(possibilities[computer])

# if choice >= 3 or choice < 0:
#     print("You typed an invalid number, you lose!") 
# elif choice == 2 and computer == 0:
#     print("You lose")
# elif computer == 2 and choice == 0 :
#     print("You win")
# elif choice > computer:
#     print("You win")
# elif computer > choice:
#     print("You lose")
# elif computer == choice:
#     print("Draw")