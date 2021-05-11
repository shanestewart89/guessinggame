
import random
scores = [10]

def start_game():
  number = random.randrange(1,11)
  attempt_count = 1
  print("The current high score is {} tries.".format(min(scores)))
  try:
    guess = int(input("{}, guess a number between 1 and 10 ".format(name)))
    while guess != number:
       if guess > number:
          print("It's lower, guess again.")
          attempt_count += 1
          guess = int(input("{}, guess a number between 1 and 10 ".format(name)))
          
       elif guess < number: 
          print("It's higher, guess again.")
          attempt_count += 1
          guess = int(input("{}, guess a number between 1 and 10 ".format(name)))
        
  except ValueError:
    
    print("That's not a number between 1 and 10. Try again!")
    start_game()
    
  else:
    
        
    
    print("That's it!")
    print("It took you {} attempts.".format(attempt_count))     
  
    scores.append(attempt_count)
  
    
    
    play_again = input("Would you like to play again? (yes/no) ")

    if play_again == 'yes':
      start_game()
  
    else:
      print("Goodbye.")  
    
print("*** ??? THE GUESSING GAME ??? ***")    
name = input("Hello, what is your name? ")
print("Hi, {}. Welcome to the Guessing Game!".format(name))
  



start_game()

