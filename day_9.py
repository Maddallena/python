# DICTIONARIES, NESTING AND THE SECRET AUCTION
# from replit import clear

# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
# }

# # # Retriving items from dictionary
# # print(programming_dictionary["Bug"])

# # # Adding new items to dictionary
# # programming_dictionary["Loop"] = "The action of doing something over and over again."

# # # Create an empty dictionary
# # empty_dictionary = {}

# # # Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Zadanie1

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇

# for student in student_scores:
#     grade = student_scores[student]
#     if grade > 90:
#         student_grades[student] = "Outstanding"
#     elif grade > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif grade > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"


# # 🚨 Don't change the code below 👇
# print(student_grades)

# nesting a list into the dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }

# nesting Dictionary in a list
# travel_log = [
#     {
#       "country": "France", 
#       "cities_visited": ["Paris", "Lille", "Dijon"], 
#       "total_visits": 12
#     },
#     {
#       "country": "Germany",
#       "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#       "total_visits": 5
#     }
# ]

# zadanie 2

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country_visited, times_visited, cities_visited):
#     # to było moje rozwiązanie:
#     # new_country = {"country": country, "visits": visits, "cities": cities} 
#     # travel_log.append(new_country)
#     # rozwiązanie z kursu:
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)




# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# #########################################################################################################################################################################















# zadanie 3
from os import system, name
def clear():
    if name == "nt":
        _ = system("cls")


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''



print(logo)


bidding_game = {}
more = True
max = 0
while more:
    bidder_name = input("What is your name?: ")
    how_much = int(input("What is your bid?: $"))
    bidding_game[bidder_name] = how_much

    other_bidders = input("Are there any other bidders? Type 'yes or 'no'. ")
    if other_bidders == "yes":
        more = True
        clear()
    else:
        clear()
        more = False
 
for person in bidding_game:
    bid = bidding_game[person]
    if bid >= max:
        max = bid

for key, value in bidding_game.items():
    if value == max:
        print(f"{key} is the winner with {value} price!")

print(id(max))
    



