# To audit a standard list of monthly pantry items and generate a 
# specific shopping list for items that are out of stock.

monthly_pantry_items = ["Milk", "Eggs", "Bread", "Apples", "Coffee"]
final_list={}

print("1. Add items only")
print("2. Review/Audit only")
print("3. Do both (Add then Review)")
choice = int(input("Select an option (1, 2, or 3): "))

if choice in [1,3]:
    add = 'Y'
    while add == 'Y':
        items=input('Enter the item to add to the list')
        monthly_pantry_items.append(items)
        add=input('Do you want to continue adding items to the list,(Y/N)').upper()

if choice in [2,3]:
    print('\n Monthly Review')  
    for i in monthly_pantry_items:
        res = input(f'Did you find {i} (y/n): ').upper()
        if res == 'N':
            quantity=input(f'Enter the quantity to buy ')
            final_list[i]=quantity
        else:
            print('Great! You have enough.')

if choice == 1:
    print(f"\nUpdated Master List: {monthly_pantry_items}")
elif final_list:
    print(f"\nFinal Shopping List: {final_list}")
else:
    print("\nEverything is in stock!")