# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100], # Week 1
    [180, 60, 110], # Week 2
    [220, 55, 105], # Week 3
    [210, 65, 95]   # Week 4
]

# Initialize variables to store the sums
food_total = 0
transport_total = 0
utilities_total = 0
weekly_totals = [] 
grand_total = 0

# Calculates expenses
# Use loop statements
for week in monthly_expenses:
    # 1. Calculate specific category totals (Columns)
    food_total += week[0]      # Index 0 is Food
    transport_total += week[1] # Index 1 is Transport
    utilities_total += week[2] # Index 2 is Utilities
    
    # 2. Calculate sum for the specific week (Rows)
    current_week_sum = 0
    for expense in week:
        current_week_sum += expense
        
    # Add this week's sum to the list of weekly totals
    weekly_totals.append(current_week_sum)
    
    # 3. Add to the grand total for the month
    grand_total += current_week_sum

# Print expenses
print('MONTHLY EXPENSES')
print('------------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', weekly_totals[0])
print('Week 2:', weekly_totals[1])
print('Week 3:', weekly_totals[2])
print('Week 4:', weekly_totals[3])
print('------------------')
print('TOTAL:', grand_total)