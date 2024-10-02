'''
## Bonus 1
'''

wieght = float(input("Enter your wieght in (kg): "))
height = float(input("Enter your height in (cm): "))/100
bmi=wieght/(height**2)

print("Your BMI is: ",round(bmi,1))

if bmi< 18.5:
    print("You are underweight. Watch your health.")
elif bmi>= 18.5  and bmi<=24.9:
    print("You are fit & healthy.")
else:
     print("You are overwieght you need to work out more and watch your diet.")   