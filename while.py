# import random
from random import  randrange

# make a list

farmAnimals =["Goat", "Sheep", "Horse", "Duck", "Cow"]
random_number = randrange(5)
random_animal = farmAnimals[random_number]

print("I am thinking of a farm animal, can you guess?")
input_farmAnimal = input("Which animal do you think?")


number_of_guesses = 1

while input_farmAnimal != random_animal:
    print ("Not correct,",input_farmAnimal, "is not the one!")
    input_farmAnimal =input ("try another farm animal")
    number_of_guesses +1

print ("Yes! It was the", random_animal, "It took you" ,number_of_guesses)