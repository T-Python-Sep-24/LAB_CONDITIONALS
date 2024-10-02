#Take user input for their weight
weight: float = float(input("Please enter your weight in kg: "))

#Take user input for their height
heightCm: float = float(input("Please enter your height in cm: "))

#To get height in meters
heightMeters: float = heightCm / 100

#Calculate BMI
bmi: float = round(weight / (heightMeters**2), 2)

#Print results to user
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight. Watch your health")
elif bmi >= 18.5 and bmi <=24.9:
    print("You are healthy")
else:
    print("You are overweight. Workout more and watch your diet")
