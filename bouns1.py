
weight:float = float(input("weight(kg): "))
height:float = float(input("height(m): "))
BMI = weight / (height*height)
if BMI >= 25 :
    print("You are overwieght you need to work out more and watch your diet")
elif BMI < 25 and BMI >= 18.5 :
    print("You are fit & healthy.")
elif BMI < 18.5 :
    print("You are underweight. Watch your health.")
