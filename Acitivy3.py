height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

BMI = weight / (height/100)**2

print("Your BMI is",BMI)

if BMI <= 18.4:
    print("You are underweight")

elif BMI <= 24.9:
    print("You are weight")

elif BMI <= 29.9:
    print("You are over weight")

elif BMI <= 34.9:
    print("You are severely over weight")

elif BMI <= 39.9:
    print("You are obese")

else:
    print("You are severely obese")