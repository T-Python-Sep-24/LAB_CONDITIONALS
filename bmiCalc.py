'''
- Ask the user to provide his wieght.
- Ask the user to provide hi height.
- print the BMI for the user.
- using conditionals tell the user that either :
- - You are overwieght you need to work out more and watch your diet.
- - You are fit & healthy.
- - You are underweight. Watch your health.
bmi=kg/h^2
'''
Weight =float(input("What is your Weight in KG: "))
height =float(input("What is your height in CM: "))/100
BMI=Weight/(height**2)

print (f"Your BMI is : {BMI:.2f} and thats mean: \n")

if BMI>=25:
    print("You are overwieght you need to work out more and watch your diet.")
elif 18.5 <= BMI<=24.9 :
    print("You are fit & healthy.")
elif BMI<=18.5:
    print("You are underweight. Watch your health.")
