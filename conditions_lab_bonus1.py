print("----- Welcome to my BMI calculator -----")
weight = float(input("Enter your weight in (kg ie. 65): "))
height = float(input("Enter your Height in (meters ie. 1.66): "))

# Formula: BMI =  weight / height^2

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

'''
    Classifications, numbers, and formula are referenced from 
    https://www.diabetes.ca/resources/tools-resources/body-mass-index-(bmi)-calculator
'''

if bmi < 18.5:
    print("You are classified as Underweight, which may increase the RISK of developing health problems")
elif 18.5 < bmi < 24.9:
    print("Nice, you are at the normal range of weight, we hope you keep it that way to avoid health problems")
elif 25.0 < bmi < 29.9:
    print("You are classified as OVERWEIGHT, which may INCREASE the RISK of developing health problems")
    print("watch your weight, and maintain a healthier life style and workout")
elif 30 < bmi < 34.9:
    print("You are classified as OBESE CLASS I, which may have HIGH RISK of developing health problems")
    print("Be careful, your at risk please consider visiting the Nutritionist and take regular health checks")
elif 35 < bmi < 39.9:
    print("You are classified as OBESE CLASS II, which may have VERY HIGH RISK of developing health problems")
    print("Be careful, your at risk please consider visiting the Nutritionist and take regular health checks")
elif bmi > 40:
    print("You are classified as OBESE CLASS III, which may have EXTREMELY HIGH RISK of developing health problems")
    print("Be careful, your at risk please consider visiting the Nutritionist and take regular health checks")