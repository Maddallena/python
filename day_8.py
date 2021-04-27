# FUNCTION PARAMETERS

import math

# def greet(): #create the function
#     print("Hello")
#     print("My name's Magda.")
#     print("How are you?")

# greet() #call the function

# # FUNCTION THAT ALLOWS THE INPUT
# def greet_with_name(name):
#     print(f'Hello {name}!')
#     print(f'How do you do {name}.')

# greet_with_name("Magdalena")

# W środku funkcji, to co bierzemy z nawiasów nazywamy parametrami, a to co wpisujemy, kiedy wywołujemy to argument(bo to jest wartość tych danych, które chcemy przetworzyć)

# def greet_with(name, location):
#     print(f'Hello {name} from {location}!')
    
# greet_with("Magdalena", "Tatry") # positional argument - ważna jest pozycja argumentu! jeśli chce się nie utrzymać kolejności a zochować wartości: name = Magdalena, location = Tatry, wtedy nie są positional arguments a key word argumentes

# greet_with(location = "Tatry", name = "Magdalena")

# # Zadanie 1

# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You will need {number_of_cans} cans of paint.")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# # Zadanie 2

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)

# Zadanie 3 Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_lenght = len(alphabet)

def caesar(text, shift, direction):
    new_text = ""

    if shift > alphabet_lenght:
        shift = shift % alphabet_lenght

    if direction == "decode":
            shift *= -1
    
    for position in range(len(text)):
        letter = text[position]
      
        if letter  not in alphabet:
            new_text += letter
        else:
            new_position =  alphabet.index(letter) + shift

            if new_position >= alphabet_lenght:
                shift_2 = new_position - alphabet_lenght
                new_letter = alphabet[shift_2]
            else:
                new_letter = alphabet[new_position]
        
            new_text += new_letter

    print(f"The {direction}d text is {new_text}.")

go = True

while go:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        choice = input("Do you want another go? If yes just let me know, if no then type: no - ").lower()
        if choice == 'no':
            go = False
            print("ok, bye bye.")
    else:
        print("Wrong command, try again")



        

    
  






  






