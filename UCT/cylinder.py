#Rob Haynes
#10 May 2021

import math

def circle_area(diameter):
    return 0.25*math.pi*(diameter*diameter)

def cylinder_volume(diameter, height):
    return circle_area(diameter)*height

def main():
    diameter = eval(input("Enter diameter:\n"))
    height = eval(input("Enter height:\n"))

    print("The volume of the cylinder is ",end='')
    print('{:.2f}'.format(cylinder_volume(diameter, height)))

if __name__=='__main__':
    main()