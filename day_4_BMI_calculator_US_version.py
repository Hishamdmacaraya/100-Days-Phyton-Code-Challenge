print("Welcome to the 'BMI Calculator (US version)'")
print(' ')



height = float(input("What's is your height in inches?\n(in)  ")) 

print(' ')
weight = float(input("What's is your weight in Pound?\n(lbs)  ")) 

print(' ')
print('Calculating......')

BMI = round(((weight / height ** 2) * 730), 2)
BMI_str = str(BMI)


print(' ')
print('----------------------------------')
print('Your BMI is:  ' + BMI_str)
print(' ')

print('According to CDC, your BMI means:')
if BMI <= 18.5:  
    print("You are underweight")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy")  
elif BMI <= 29.9:  
    print("You are overweight")  
else:  
    print("You are obese")  
print('----------------------------------')

print(' ')
print('Adult Body Mass Index or BMI Table from CDC')
print(' ')

from tabulate import tabulate


data = [["Underweight", '18.5'], 
        ["Normal", '18.5 - 24.9'], 
        ["Overweight", '25.0 - 29.9'], 
        ["Obese", '30 and above']]
  
#define header names
col_names = ["Weight Status", "BMI"]
  
#display table
print(tabulate(data, headers=col_names, tablefmt="fancy_grid")) 

print(' ')
print('Reference: https://www.cdc.gov/healthyweight/assessing/index.html')
