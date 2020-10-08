#! /usr/bin/env Python3

# author: python.wonder.woman@gmail.com
# EN version
# calculator BMI with input from the console
# BMI pattern = weight/height^2

def gather_info():
    weight = float(input("Let us know how is your weight? (kilograms) "))
    height = float(input("\nHow tall are you? (meters)? "))
    return(weight, height)

def calculate_bmi(weight, height):
    bmi = (weight / (height ** 2))
    return(bmi)

while True:
    weight, height = gather_info()
    bmi = calculate_bmi(weight,height=height)
    print(bmi, weight,height, calculate_bmi(weight,height))
    if bmi < float(18.5):
        print("Your weight is too low.")
    elif bmi >= float(25):
        print("Your weight is too high.")
    else:
        print("Your weight is perfect. Congrats and keep going!")
    print(f"Your BMI is: {bmi:.2f}")
    print("\n\nIf you have got any questions do not hesitate to contact me at python.wonder.woman@gmail.com")
    break
