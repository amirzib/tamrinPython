appetizer = ['soup','mirza ghasemi','kookoo sabzi','ash-e Jo']
food = ['pizza','hamberger','hotdog','spagetti']
drink=['cola','fanta','sprite','water']
for i in appetizer:
    print (i,end="  ")
appetizerCustom = input("\nEnter ur chooise: ")
newAppertizerCustom=appetizerCustom.lower().strip()
indexOfAppetizer = appetizer.index(newAppertizerCustom)
print(f"your chooise is: {appetizer[indexOfAppetizer]}")

for j in food:
    print (j,end="  ")
foodCustom = input("\nEnter ur chooise: ")
newFoodCustom=foodCustom.lower().strip()
indexOfFood = food.index(newFoodCustom)
print(f"your chooise is: {food[indexOfFood]}")

for z in drink:
    print (z,end="  ")
drinkCustom = input("\nEnter ur chooise: ")
newDrinkCustom=drinkCustom.lower().strip()
indexOfDrink = drink.index(newDrinkCustom)
print(f"your chooise is: {drink[indexOfDrink]}")