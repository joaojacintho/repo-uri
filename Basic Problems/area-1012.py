"""

Problem: 1012
Author: João Lucas
URI Online Judge

"""

a, b, c = input().split()

a = float(a)

b = float(b)

c = float(c)

pi = 3.14159

triangled = 0.5 * a * c
print("TRIANGULO: {:.3f}".format(triangled))

radius_circle = pi * c ** 2
print("CIRCULO: {:.3f}".format(radius_circle))

trapezium = 0.5 * c * (a + b)
print("TRAPEZIO: {:.3f}".format(trapezium))

square = b ** 2
print("QUADRADO: {:.3f}".format(square))

rectangle = a * b
print("RETANGULO: {:.3f}".format(rectangle))