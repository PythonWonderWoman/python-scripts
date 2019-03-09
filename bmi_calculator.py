#! /usr/bin/env python

#calculator BMI with input from the console
#BMI pattern = weight/wzrost^2

print("Let us know how is your weight: ")
weight = int(input()) #kg

print("How tall are you?")
height = float(input()) #cm

#calculate BMI
bmi = (weight / (height ** 2))

print("Your BMI value is: ", "%.2f" % bmi) #rounding u to two decimal places