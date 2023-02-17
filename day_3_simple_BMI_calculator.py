print("Welcome to the 'Simple BMI Calculator'")
print(' ')

height = float(input("What's is your height in meters?\n")) 

print(' ')
weight = float(input("What's is your weight in Kilograms?\n")) 

print(' ')
print('Calculating......')

BMI = weight / height ** 2
BMI_str = str(BMI)


print(' ')
print('-------------------------')
print('Your BMI is:  ' + BMI_str)
print('-------------------------')
