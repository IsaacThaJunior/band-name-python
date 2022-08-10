
# Build a prime number checker function
def is_prime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
        if prime:
          print(f'{num} is a prime number')
        else:
          print(f'{num} is not a prime number')

n = int(input('Check this number: '))
is_prime(num=n)
