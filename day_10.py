# Functions with Outputs
# mój przykład
# def format_name(f_name, l_name):
#     # f_name = input("What is your first name?: ").lower()
#     # l_name = input("What is your last name?: ").lower()

#     return (f_name + " " + l_name).title()


# print(format_name("magdalena", "rajewska"))

# z kursu

# #Functions with Outputs
# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   f"Result: {formated_f_name} {formated_l_name}"

# #Storing output in a variable
# formatted_name = format_name(input("Your first name: "), input("Your last name: "))
# print(formatted_name)
# #or printing output directly
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# #Already used functions with outputs.
# length = len(formatted_name)

# #Return as an early exit
# def format_name(f_name, l_name):
#   """Take a first and last name and format it 
#   to return the title case version of the name."""
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs."
#   formated_f_name = f_name.title()
#   formated_l_name = l_name.title()
#   return f"Result: {formated_f_name} {formated_l_name}"


# zadanie 1

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#     """ funkcja daje ilość dni w danym miesiącu"""
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     if month > 12 or month < 1:
#         return "Invalid month entered."
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month-1]
    

# # (moje)
# #   ind = check_month - 1
# #   if is_leap(year) == True:
# #       if ind == 1:
# #           return "That february has 29 days"   
# #   else:
# #       return month_days[month - 1]

  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


# Calculator

# # Add
# def add(n1, n2):
#     return n1 + n2

# # Substract
# def substract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+": add,
#     "-": substract,
#     "*": multiply,
#     "/": divide}

# def calculator(num1, num2):  
#     calculation_function = operations[operation_symbol]

#     answer = calculation_function(num1, num2)

#     print(f"{num1} {operation_symbol} {num2} = {answer}")

#     return answer
    
    

# go_on = False
# while not go_on:

#     num1 = int(input("What's the first number?: "))

#     for symbol in operations:
#         print(symbol)


#     operation_symbol = input("Pick an operation from the line above: ")

#     num2 = int(input("What's the second number?: "))

#     result = calculator(num1, num2)

#     decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ").lower  

#     if decision == "y":
#         next = int(input("What's the next number?: "))
#         calculator(result, next)
#         go_on = False
#     else: 
#         go_on = True


# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide}

for symbol in operations:
    print(symbol)

def calculator(num1):  

    symbol = input("Pick an operation: ")

    next_num = int(input("What's the next number?: ")
    
    calculation_function = operations[symbol]

    answer = calculation_function(num1, next_num)

    print(f"{num1} {symbol} {next_num} = {answer}")

    return answer

    
num1 = int(input("What's the first number?: "))

go_on = False      
while not go_on:

    result = calculator(num1)

    decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ").lower()

    if decision == "y":
        calculator(result)
        go_on = False

    else: 
        go_on = True