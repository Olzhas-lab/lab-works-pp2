import math
#Exercis1----------------------------------------------------
Degree = input("Enter degree: ")
Radian = float(Degree) * math.pi /180
print(Radian,"radian")
#Exercis2----------------------------------------------------
Height = input("Enter height: ")
First_Base = input("Enter first base: ")
Second_Base = input("Enter second base: ")
Trapezoid_Area = (float(First_Base) + float(Second_Base)) * float(Height) / 2
print("Area of your trapezoid is",Trapezoid_Area)
#Exercis3----------------------------------------------------
Sides_Number = input("Enter number of sides: ")
Lenght = input("Enter the length of a side: ")
Angle_per_side = 180/float(Sides_Number)
Radius = float(Lenght) / (2 * math.floor(math.tan(Angle_per_side)))
print(Radius)
Polygon_Area = (float(Sides_Number)/2) * float(Lenght) * float(Radius)
print("Area of your polygon is",Polygon_Area)
#Exercis4----------------------------------------------------
Lenght_of_Base = input("Enter length of base: ")
Height_of_Parallelogram = input("Enter height of parallelogram: ")
Parallelogram_Area = float(Lenght_of_Base) * float(Height_of_Parallelogram)
print("The area of the polygon is",Parallelogram_Area)