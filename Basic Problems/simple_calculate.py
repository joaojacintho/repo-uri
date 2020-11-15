"""

Problem: 1010
Author: João Lucas
URI Online Judge

"""

line = input().split()
cod = int(line[0])
parts = int(line[1])
value_parts = float(line[2])

line_2 = input().split()
cod_2 = int(line_2[0])
parts_2 = int(line_2[1])
value_parts_2 = float(line_2[2])

value_pay = (parts * value_parts) + (parts_2 * value_parts_2)

print("VALOR A PAGAR: R$", '{:.2f}'.format(value_pay))

