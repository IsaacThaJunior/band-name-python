print('Welcome to Python Pizza Deliveries!')

size = input('What size pizza do you want? (S, M, L) ')
add_pepperoni = input('Do you want pepperoni? (Y/N) ')
extra_cheese = input('Do you want extra cheese? (Y/N) ')

your_bill = 0

if size == 'S':
    your_bill += 10
elif size == 'M':
    your_bill += 15
elif size == 'L':
    your_bill += 20

if add_pepperoni == 'Y':
  if size == 'S':
    your_bill += 2
  else:
    your_bill += 3

if extra_cheese == 'Y':
  your_bill += 1


print(f'Your bill is ${your_bill}')