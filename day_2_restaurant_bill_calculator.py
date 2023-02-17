print("Welcome to the 'Simple Restaurant Bill Calculator!'")
print(' ')

bill = float(input("What was the total bill?\n$"))
print(' ')
tip = int(input("How much tip would you like to give? 10%, 12%, or 15%?\n(%) "))
print(' ')
tax_rate = float(input("What was your tax rate?\n(%) "))
print(' ')
people = int(input("How many people to split the bill?\n"))


tip_as_percent = tip / 100
tax_as_percent = tax_rate / 100
total_tip_amount = bill * tip_as_percent
total_bill_plus_tax = bill * tax_as_percent
total_bill = bill + total_tip_amount + total_bill_plus_tax
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
tax_due = tax_as_percent  * bill

print(' ')
print('-------------Total Bill-------------')
print('')

print(f"Total payment due:         ${total_bill}")
print(f"Total tax due:             ${tax_due}")
print(f"Payment due per person:    ${final_amount}")
print(' ')

print(' ')
print('-------------End-------------')
