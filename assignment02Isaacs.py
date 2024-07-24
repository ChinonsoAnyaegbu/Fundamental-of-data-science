toDoList =["Wake up by 7am", "Meditate", "Freshen up", "Eat breakfast", "Start my project", "Call John" ]
print (toDoList)

# Add task
toDoList.append("Go for a walk")
print (toDoList)

# Add task with an input
new_task = input("What do you want to add to the list?")
toDoList.append(new_task)
print (toDoList)

# Number of tasks in toDoList
toDoList
length = len(toDoList)
print ("Number of tasks in toDoList:", length)

# Remove first task
toDoList.pop(0)
print(toDoList)

#Remove specific task (Meditate)
if "Meditate" in toDoList:
 toDoList.remove("Meditate")
print(toDoList)

# Inform the user based on the number of tasks they have left

if length < 4:
 print ("You have time to do more tasks!")
elif length >= 6:
  print("You do not have time to do more tasks")

