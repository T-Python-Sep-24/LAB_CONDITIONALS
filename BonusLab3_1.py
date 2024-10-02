# Bouns 1 for Lab 3

#The User Input
userWieght = float (input("Please enter your wieght in KG: "))
userHight = float (input("Please enter your hight in CM: "))
userBMI = userWieght/(userHight**2)

print(f"Your BMI: {userBMI:.2f}")

#if statments
if userBMI <= 18.5:
    print("You are Underweight. Watch your Health.")

elif userBMI >= 18.5:
    print("You are Fit & Healthy.")    

else:
    print("You are Overwieght you Need to Work Out More and Watch your Diet.")    