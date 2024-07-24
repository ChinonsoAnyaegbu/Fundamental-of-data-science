criteria1= "The prototype collects/uses data from relevant source"
print(criteria1)
score1  = int (input ("what is the score?"))

criteria2= "The prototype analyses and visualizes data"
print(criteria2)
score2 = int (input("What is the score?"))

criteria3= "The prototype has a dashboard"
print(criteria3)
score3 = int (input("What is the score?"))

criteria4= "The prototype analyses and visualizes data"
print(criteria4)
score4 = int (input("What is the score?"))

criteria5= "The extended abstract and prototype address a relevant problem"
print(criteria5)
score5 = int (input("What is the score?"))

total_score = score1 + score2 + score3 + score4 + score5

if (score1 == -2):
    print("knockout on criteria 1")

if (score2 == -2):
    print("knockout on criteria 2")

if (score3 == -2):
    print("knockout on criteria 3")

if (score4 == -2):
    print("knockout on criteria 4")

if (score5== -2):
    print("knockout on criteria 5")
print(total_score)