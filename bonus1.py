'''
Calculates the BMI (body mass index) of the user:
'''

weight: float = input("weight in KG (for example: 70): ")
height: float = input("height in Meter (for example 1.75): ")

# calculate BMI
bmi = int(weight) / float(height) ** 2
print(f"BMI: {bmi:.2f}") # round into 2 decimal point

# check if overweight, underweight or healthy
if bmi > 60:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi < 18.5:
    print("You are underweight. Watch your health.")
else:
    print("You are fit & healthy")
