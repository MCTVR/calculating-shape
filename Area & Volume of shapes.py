"""
MADE BY MCTVR
OPEN SOURCED
AVAILABLE ON GITHUB ONLY!!!
EASY FOR BEGINNERS
AREA & VOLUME CALCULATOR
PYTHON 3.9
"""

import time #import time library
print("\nCalculate the area(s) or volume of shapes!\n") #Introduction to the program
MU = input("Enter the Measurement unit for your shape (e.g. cm, m, km): ") #Enter your Measurement Unit here

def Square(): #Function calculating Square area
    side = float(input("\nEnter the height of the Square: "))
    print("\nArea: ", side * side, MU + "^2")

def Rectangle(): #Function calculating Rectangle area
    height = float(input("\nEnter the height of the Rectangle: "))
    width = float(input("\nEnter the width of the Rectangle: "))
    print("\nArea: ", height * width, MU + "^2")

def Triangle(): #Function calculating Triangle area
    height = float(input("\nEnter the height of the Triangle: "))
    base = float(input("\nEnter the base of the Triangle: "))
    print("\nArea: ", (height * base) / 2, MU + "^2")

def Trapezium(): #Function calculating Trapezium area
    ub = float(input("\nEnter the upper base of the Trapezium: "))
    lb = float(input("\nEnter the lower base of the Trapezium: "))
    height = float(input("\nEnter the height of the Trapezium: "))
    print("\nArea: ", ((ub + lb) * height) / 2, MU + "^2")

def Circle(): #Function calculating Circle area
    pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233
    radius = float(input("Enter the radius of the Circle: "))
    area = radius * radius * pi
    print("\nArea ≈", round(area, 2), MU + "^2 (Rounded to the second digit)")

def Rhombus(): #Function calculating Rhombus area
    diag = float(input("Enter the one diagnal of the Rhombus: "))
    diag1 = float(input("Enter the other diagnal of the Rhombus: "))
    print("\nArea: ", (diag * diag1) / 2, MU + "^2")

def Cube(): #Function calculating cube volume
    side = float(input("\nEnter the height of the Square: "))
    print("\nArea: ", side * side * side, MU + "^3")

def Rectangle3(): #Function calculating Rectanglar prism volume
    height = float(input("\nEnter the height of the Rectangle: "))
    length = float(input("\nEnter the length of the Rectangle: "))
    width = float(input("\nEnter the width of the Rectangle: "))
    print("\nArea: ", width * length * height, MU + "^3")

def Pyramid(): #Function calculating Pyramid volume
    height = float(input("\nEnter the height of the Pyramid: "))
    basew = float(input("\nEnter the base width of the Pyramid: "))
    basel = float(input("\nEnter the base length of the Pyramid: "))
    print("\nArea: ", (basel * basew * height) / 3, MU + "^3")

def Sphere(): #Function calculating Sphere volume
    pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233
    radius = float(input("Enter the radius of the Circle: "))
    volume = (4 / 3) * pi * (radius * radius * radius)
    print("\nArea ≈", round(volume, 2), MU + "^3 (Rounded to the second digit)")

while True: #While loop for the main program
	#Select which shape to calculate
    choose = int(input("""
    What shape you want to calculate?
    1 : Square
    2 : Rectangle
    3 : Triangle
    4 : Trapezium
    5 : Circle
    6 : Rhombus
    7 : Cube (Volume)
    8 : Rectangle (Volume)
    9 : Pyramid (Volume)
   10 : Sphere (Volume)

    Enter (1/2/3/4/5/6/7/8/9/10):
    """))
	#Logical Operation for detecting the selection of shapes and then execute the function
    if choose == 1:
        Square()
        time.sleep(3)
    elif choose == 2:
        Rectangle()
        time.sleep(3)
    elif choose == 3:
        Triangle()
        time.sleep(3)
    elif choose == 4:
        Trapezium()
        time.sleep(3)
    elif choose == 5:
        Circle()
        time.sleep(5)
    elif choose == 6:
        Rhombus()
        time.sleep(3)
    elif choose == 7:
        Cube()
        time.sleep(3)
    elif choose == 8:
        Rectangle3()
        time.sleep(3)
    elif choose == 9:
        Pyramid()
        time.sleep(3)
    elif choose == 10:
        Sphere()
        time.sleep(3)
    else: #If input is not in (1,2,3,4,5,6,7,8,9,10) ,print not valid and try again 
        print("Input not valid, Please choose again.")
        time.sleep(3)

"""
MADE BY MCTVR IN HONG KONG
VERSION 1.1
WILL UPDATE TO CALCULATE MORE SHAPES
"""