weight=int(input("what is your weight?:"))
height=int(input("what is ur Height?:"))
bmi= weight/height**2*10000
print(f"your BMI is:{round(bmi,2)}")
if bmi<=18.5:
    print("You are underweight. Watch your healtht")
elif bmi<=24.9:
    print("You are fit & healthy")
else:
    print("You are overwieght you need to work out more and watch your diet.")