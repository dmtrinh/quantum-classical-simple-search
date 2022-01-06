import random

MIN_NUM = 0
MAX_NUM = 4095

print("Welcome to the Classical Guessing Game (with hints!)")

# Generate a random integer
secret = random.randint(MIN_NUM, MAX_NUM)
print("I'm thinking of a number between %d and %d" %(MIN_NUM,MAX_NUM))

guess = -1

while True:
  guess = input("  What's your guess?  ")
  guess = int(guess)
  if (guess > secret):
    print("%d was too big, go lower!" %(guess))
  elif (guess < secret):
    print("%d was too small, go higher!" %(guess))
  else:
    print("You got it!  My secret number was %d." %(secret))
    break