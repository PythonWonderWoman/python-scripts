#! /usr/bin/env python

#author: python.wonder.woman@gmail.com
#wersja PL

#obliczenie zapotrzebowania kalorycznego (PPM) wg wzoru Harrisa Benedicta, dla kobiet i mezczyzn

#PPM_kobiety = 665.09 + 9.56 x masa ciała + 1.85 x wzrost w cm – 4.68 x wiek
#PPM_mezczyzni = 66.47 + 13.75 x masa ciała + 5 x wzrost w cm – 6.75 x wiek

print("Let us know how is your weight:\nYou can also use decimal value: 50.6 (kg):")
weight = float(input()) #kg

print("How tall are you?\nUse the following format, for example: 1.64 (cm):")
height = float(input()) #cm

print("How old are you?")
age = int(input()) #years

print("What is your sex: F/M")
sex = str(input())

query = "\n\nEnter the below value if true\n1. Sitting work, no physical activity - 1\n2. Non-physical work, not very active lifestyle - 2\n3. Light physical work, regular exercises 3-4 times a week - 3\n4. Physical work, regular exercises more that 5 times a week - 4\n5. Physical hard work, regular exercises every day - 5"

if sex == "F":
    PPM = 665.09 + (9.56 * weight) + (1.85 * height) - (4.68 * age)
    print("Your PPM value is: ", "%.2f" % PPM)
elif sex == "M":
    PPM = 66.47 + (13.75 * weight) + (5 * height) - (6.75 * age)
    print("Your PPM value is: " , "%.2f" % PPM)
else:
    print("Enter correct value F if female or M if male.")