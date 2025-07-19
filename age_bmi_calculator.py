# Age & BMI Calculator

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
weight_kg = float(input("Enter your weight in kilograms (e.g. 65.5): "))
height_cm = float(input("Enter your height in centimeters (e.g. 170): "))

current_year = 2025
age = current_year - birth_year

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\nSummary:")
print(f"Name     : {name}")
print(f"Age      : {age} years")
print(f"BMI      : {bmi:.2f} ({category})")