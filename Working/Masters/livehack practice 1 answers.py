'''
|**********************************************************************;
* Project           : Livehack #1
*
* Program name      : First practice livehack
*
* Author            : Matthew Cheung
*
* Date created      : 20190326
*
* Purpose           : Figure out if the triangle given is a right-angle triangle
|**********************************************************************;
'''

first_side = int(input("What is the length of the first side? "))
second_side = int(input("What is the length of the second side? "))
third_side = int(input("What is the length  of the third side? "))

if (first_side > second_side and third_side) and (first_side**2 == second_side**2 + third_side**2):
    print("It is a right-angled triangle.")

elif (second_side > first_side and third_side) and (second_side**2 == first_side**2 + third_side**2):
    print("It is a right-angled triangle.")

elif (third_side > second_side and first_side) and (third_side**2 == second_side**2 + first_side**2):
    print("It is a right-angled triangle.")

else:
    print("It is not a right angled triangle.")
