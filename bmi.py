# calculating the BMI

height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

bmi = weight / (height ** 2)

# casting the type to an integer and printing
print(int(bmi))
