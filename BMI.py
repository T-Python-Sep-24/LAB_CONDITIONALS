#Ask the user to provide his wieght.
wieght:str=input("Enter your wieght in kg:")
#Ask the user to provide hi height.
height:str=input("Enter your height cm:")

try:
# Convert the weight and height to Calculate BMI 
    wieght = float(wieght)
# Convert height to meters
    height = float(height) / 100

# Check for valid weight and height inputs
    if wieght <= 0 or height <= 0:
        print("Invalid input! Weight and height must be positive numbers.")
    else:
# Calculate BMI
        bmi = wieght / (height ** 2)

#print the BMI for the user.
    print(f"Your wieght: {wieght} KG")
# Convert height to meters
    print(f"Your hieght: {height * 100} CM")
    print(f"Your BMI is: {bmi:.2f}") 

# BMI between 25.0 - 39.9 is overwieght !
    if bmi >= 25.0 and bmi < 39.9:
        print("You are overwieght you need to work out more and watch your diet")
# BMI between 18.5 - 24.9 is fit & healthy
    elif bmi >= 18.5 and bmi < 24.9: 
        print("You are fit & healthy")
# BMI less than 18.5 is underweight 
    elif bmi < 18.5:
        print("You are underweight. Watch your health.")
    
except ValueError:
    print("BMI value is outside the expected range. Please check your inputs.")
    



