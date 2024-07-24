quantityConsumed = int(input("How many cookie(s) did you eat?"))
print("You ate", quantityConsumed, "cookie(s).")

caloriesPerServing = 160
# 3 cookies makes one serving
caloriesPerCookie = caloriesPerServing / 3

# Nutritional information per cookie
sodiumPerCookie= 190 /3 #mg
totalFatPerCookie = 7/3 #g
totalCarbohydratePerCookie = 25/3 #g
proteinPerCookie = 2/3 #g

# Calculate total calories consumed
totalCaloriesConsumed = quantityConsumed * caloriesPerCookie
# display total calories consumed
print ("Total calories consumed:" , totalCaloriesConsumed, "kcal" )

# Display other nutritional information
totalSodiumConsumed = quantityConsumed * sodiumPerCookie
totalFatConsumed = quantityConsumed * totalFatPerCookie
totalCarbohydrateConsumed = quantityConsumed * totalCarbohydratePerCookie
totalProteinConsumed = quantityConsumed * proteinPerCookie

print("Total sodium consumed:", totalSodiumConsumed, "mg")
print("Total fat consumed:", totalFatConsumed, "g")
print("Total carbohydrate consumed:", totalCarbohydrateConsumed, "g")
print("Total protein consumed:", totalProteinConsumed, "g")

# Check if total calorie intake exceeds 2000 kcal
if(totalCaloriesConsumed > 2000):
    print("Stop eating those darn cookies")
else:
    print("You should consider stopping here")
