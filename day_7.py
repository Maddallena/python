# HANGMAN!
import random
from hangman_words import word_list
from hangman_art import stages, logo
# from hangman_art import logo


end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range (word_length):
  display += "_"

guesses = []

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in guesses:
      print(f'You have already guessed {guess}')
  else:
    for position in range (word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
    
    if guess not in chosen_word:
      print(f'You guessed {guess}, thats not in the word. You lose a life.')
      lives -= 1 
        
      if lives == 0:
        end_of_game = True
        print("You lose.")

  guesses += guess
  # print(guesses)

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game == True
    print("You win.")
    
  print(stages[lives])
