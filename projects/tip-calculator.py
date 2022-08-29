# Creating a tip calculator

print('Welcome to the tip calculator!')

total_bill = float(input('What is the total bill? $'))
tip_percent = int(input('What is the tip percentage? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

bill_with_tip = (tip_percent / 100)
complete_tip = total_bill * bill_with_tip
complete_bill_with_tip = complete_tip + total_bill
per_person = round(complete_bill_with_tip / people, 2)

print(f'Each person should pay ${per_person}.')
