#DZIEŃ PIĄTY___________________________________________________________________________________________________________________________________________

#for loops
# for item in list_of_items - do sth to each of them

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)


#Zadanie1 average height
 
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])


# heights_sum = 0
# for a in student_heights: # najlepiej używać w pętli nazwy (a) w liczbie pojedynczej!!!
#     heights_sum += a
# print(heights_sum)

# how_many = 0
# for b in student_heights: # w każdej pętli mogłabym mieć a, ale lepiej nadawać osobne nazwy, żeby wracając do kodu wiedzieć o co chodziło w momencie pisania 
#     how_many += 1
# print(how_many)

# average = round(heights_sum / how_many)
# print(average)


#Zadanie2 High Score

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# max = 0
# for score in student_scores:
#   if score > max:
#     max = score

# print("The highest score in the class is:", max)

#For loop with Range
# for number in range(1, 11, 3): #żeby pokazało liczby w zakresie od 1 do 10, ostatnia cyfra to krok
#   print(number)

# total = 0
# for number in range(1,101):
#   total += number
# print(total)

#Zadanie3 Adding Evens

# total = 0

# for even_number in range(1,101):
#   if even_number % 2 == 0:
#     total += even_number
# print(total)

# total2 = 0
# for even_number in range(2,101,2):
#   total2 += even_number
# print(total2)

#Zadanie4 FizzBuzz

# for number in range(1,101): # THIS LOGIC MATTERS!!!!!!
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)

#Zadanie5 Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []

for letter in range(1, nr_letters + 1):
  letter = letters[random.randint(0, len(letters)-1)]
  password.extend(letter)


for symbol in range(1, nr_symbols + 1):
  symbol = symbols[random.randint(0,len(symbols)-1)]
  password.extend(symbol)


for number in range(1, nr_numbers + 1):
  number = numbers[random.randint(0, len(numbers)-1)]
  password.extend(number)

mix_password = random.sample(password, len(password))
print(''.join(mix_password))


#ROZWIĄZANIE:
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")