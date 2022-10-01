
# try:
#     for i in ['a', 'b', 'c']:
#         print(i ** 2)
# except:
#     print('Abeg try do better operation')


# try:
#     x = 5
#     y = 0

#     z = x/y

# except:
#     print('Not you tryna divide with zero')
# finally:
#     print('All Done')

def ask():
    while True:
        try:
            number = int(input('Input an integer: '))
            squared = number**2
            print(f'Thank you, your number squared is: {squared}')
        except:
            print('An error occurred')
            print('You sef no dey read instructions')
        else:
            break
        

ask()