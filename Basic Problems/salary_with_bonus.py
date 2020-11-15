"""

Problem: 1009
Author: João Lucas
URI Online Judge

"""

name = input()

salary = float(input())

sales = float(input())

salary_with_bonus = salary + (sales * 0.15)

print('TOTAL = R$', '{:.2f}'.format(salary_with_bonus))
