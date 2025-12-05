# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   if day_number == 1:
      return meal_plan[0]
   elif day_number == 2:
      return meal_plan[1]
   elif day_number == 3:
      return meal_plan[2]
   elif day_number == 4:
      return meal_plan[3]
   elif day_number == 5:
      return meal_plan[4]
   elif day_number == 6:
      return meal_plan[5]
   elif day_number == 7:
      return meal_plan[6]
   else:
      return 'kaka'

# Prints weekly meal plan
print('WEEKLY MEAL PLAN')
print('================')
print(f'{weekday(1)}:{day_meal_plan(meal_plan,1)}')
print(f'{weekday(2)}:{day_meal_plan(meal_plan,2)}')
print(f'{weekday(3)}:{day_meal_plan(meal_plan,3)}')
print(f'{weekday(4)}:{day_meal_plan(meal_plan,4)}')
print(f'{weekday(5)}:{day_meal_plan(meal_plan,5)}')
print(f'{weekday(6)}:{day_meal_plan(meal_plan,6)}')
print(f'{weekday(7)}:{day_meal_plan(meal_plan,7)}')