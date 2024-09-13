import math
"""Things to include in Calculator:
        -arthimatic actions
        -finding area of shapes
        -maybe matrices, derviatives, integrals
        -maybe being able to find x
        -some interface with buttons if you can
"""
# Arthimatic Equations
def addition(num1,num2):
    return num1 + num2
def subtraction(num1,num2):
    return num1 - num2
def multiplication(num1,num2):
    return num1 * num2
def division(num1,num2):
    if num2 == 0:
        return "Can't divide by zero"
    else:
        return num1 / num2
    
# Areas of Shapes
def circle_area(radius):
    return math.pi * math.pow(radius,2)
def square_area(num):
    return math.pow(num,2)
def rectangle_area(num1,num2):
    return num1*num2
def triangle_area(base,height):
    return base / 2 * height


# Trig
def unit_circle(radian,trig):
    #to be worked on later, trying to figure out how to do pi
    if trig == "cos":
        pass
    elif trig == "sin":
        pass
    elif trig == "tan":
        pass
    elif trig == "csc":
        pass
    elif trig == "sec":
        pass
    elif trig == "cot":
        pass
    else:
        return "Not valid"

# finding x
def finding_x(equation):
    pass


def main():
    print("This is the main method")
# print(addition(3,4))
# print(subtraction(3,4))
# print(multiplication(3,4))
# print(division(3,4))
# print(division(3,0))
# print(circle_area(3))
main()