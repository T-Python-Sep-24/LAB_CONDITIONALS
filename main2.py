wieght_1 =float(input("enter your wieght in kg:"))
height_1=float(input("enter your height in meters:"))
bmi=wieght_1/height_1**2
print("your bmi is ",bmi)
if bmi >25 :
    print("You are overwieght you need to work out more and watch your diet.")
elif 18<=bmi<=25:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")