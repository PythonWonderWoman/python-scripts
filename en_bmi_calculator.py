#! /usr/bin/env python3

#author: python.wonder.woman@gmail.com
# EN version

#calculator BMI with input from the console
#BMI pattern = weight/height^2

print("Let us know how is your weight:\nYou can also use decimal value: 50.6 (kg):")
weight = float(input()) #kg

print("\nHow tall are you (in cm)?\nUse the following format, for example: 1.64 (cm):")
height = float(input()) #cm

#calculate BMI
bmi = (weight / (height ** 2))

print("\nYour BMI value is: ", "%.2f" % bmi) #rounding to two decimal places

if bmi < float(18.5):
    print("You have to low weight, you should consider to eat more or more efficient. The best practices you can learn from dietician.")
elif bmi >= float(25):
    print("Your weight is too high. You should consider to go to the dietician. It will have impact on your health condition in the future, if you don't slow down.")
else:
    print("Your weight is perfect. Congrats and keep going! If you have more time, share it with your friends to take care about them too :)")
#
# additional comment for users
#
print("\n\nIf you have got any questions do not hesitate to contact me at python.wonder.woman@gmail.com")