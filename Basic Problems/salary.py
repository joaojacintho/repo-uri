"""

Problem: 1008
Author: João Lucas
URI Online Judge

"""

employee_number = int(input())

worked_hour = int(input())

payment_hour = float(input())

salary = worked_hour * payment_hour

print("NUMBER =",employee_number)
print("SALARY = U$", '{:.2f}'.format(salary))
