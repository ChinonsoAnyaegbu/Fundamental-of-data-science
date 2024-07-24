from random import randrange

# set a range for random number
random_number =randrange(1,101)
# get number from user
guess = input ("Guess a number between 1 and 100:")
# typecast to int
guess = int(guess)

#check
while random_number != guess:
    if(guess > random_number):
        print("The random number is lower")
    else:
        print("The random number is higher")

    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
print("weldone! the number was", random_number)
