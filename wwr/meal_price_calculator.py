print('Meal Price Calculator')
print()
kids_meal_price = input('Price of kids meal($): ')
adults_meal_price = input('Price of adults meal($): ')
quantity_kids = input('How many kids meal? ')
quantity_adults = input('How many adults? ')
tax = float(16)
sub_total_kids_meal = float(kids_meal_price)*int(quantity_kids)
sub_total_adults_meal = float(adults_meal_price)*int(quantity_adults)
sub_total = sub_total_adults_meal + sub_total_kids_meal
tax_to_pay = sub_total*tax/100
print(tax_to_pay)
grand_total = sub_total + tax_to_pay
print(f'Total to pay is ($) {grand_total}')
amount = input('amount received($)? ')
change = float(amount) - float(grand_total)
missing = float(grand_total) - float(amount)
print(f'Change ($){change:.2f} ')
print('Thanks for passing by. Come back soon!')
