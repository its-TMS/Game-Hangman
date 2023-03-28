import random
from hangman_art import logo, stages
from hangman_words import word_list
import os

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

#Testing code
# print(f'\nPssst, the solution is {chosen_word}.')

#Create blanks
display = []
guessed_incorrect = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input(f"\nGuess a letter: ").lower()

    os.system('clear')

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You\'ve already gussed '{guess}', try again...")

    else:
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
                
      #Check if user is wrong.
      if guess not in chosen_word:
          #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

          
          print(f"You guessed '{guess}', that's not in the word. You lose a life.")
          lives -= 1
          guessed_incorrect.append(guess)
          if lives == 0:
              end_of_game = True
              print("\nYou lost!.")
  
      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
  
      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("\nYou win.")

      print(stages[lives])
    
  
    
