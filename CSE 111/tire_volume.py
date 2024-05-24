

import math

#print a description of a program
print('This program computes and outputs the volume of space inside the tire\n')


# Get the width, aspect ratio and diameter from the user

width = float(input('Enter the width of the tire in mm:'))
aspect_ratio = float(input('Enter the aspect ratio of the tire:'))
diameter = float(input('Enter the diameter of the wheel in inches:'))

#compute the volume of the tire
parenthesis = width * aspect_ratio + 2540 * diameter
volume_of_tire = math.pi * (width**2) *aspect_ratio * parenthesis

volume_final = volume_of_tire/10000000000

#print the volume of the tire for the user to see

print(f'The approximate volume is {volume_final}')

