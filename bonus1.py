# write a program that Calculates the BMI (body mass index) of the user

userWieght=float(input("Enter your wieght:"))

userHeight= float(input("Enter your hight:"))

totalBody=  userWieght  / (userHeight ** 2)


# print(round(totalBody,2 ))

if totalBody >= 25.0 and totalBody <= 30.0 :
    print (f"need to work out more and watch your diet {round(totalBody,2)} ")

elif totalBody >= 18.5 or totalBody <= 25.0 : 
    print(f"He is fit & healthy {round(totalBody,2)} " )

elif totalBody > 16.0 and totalBody < 18.5:
    print(f"Watch your health {round(totalBody,2)}")

else:
    print("Please try another any body")