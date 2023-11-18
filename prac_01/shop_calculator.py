"""
Calculator used by shop to do simple addition of item's cost
"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_costs = 0
for i in range(number_of_items):
    item_cost = float(input("Price of item: "))
    total_costs += item_cost

if total_costs > 100:
    total_costs = total_costs*0.9

print(f"Total price for {number_of_items} items is ${total_costs:.2f}")