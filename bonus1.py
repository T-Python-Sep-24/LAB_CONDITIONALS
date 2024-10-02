#Ask the user to provide his wieght.
weight = float(input("Please enter your weight in kilograms: "))

# Ask the user for their height
height = float(input("Please enter your height in meters: "))


#BMI Function
def calculate_bmi(weight, height):
    return weight / (height ** 2)


# Calculate BMI
bmi = calculate_bmi(weight, height)

#print the BMI for the user.
print(f"Your BMI is: {bmi:.2f}")

'''- using conditionals tell the user that either :
 You are overwieght you need to work out more and watch your diet.
 You are fit & healthy.
 You are underweight. Watch your health.'''

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif 18.5 <= bmi < 24.9:
    print("You are fit & healthy.")
else:
    print("You are overweight; you need to work out more and watch your diet.")