wieght = float(input("enter your wieght : "))
height = float(input("enter your height in meters : "))


bmi = round(wieght / (height**2),2)

print(bmi)
     
if bmi  < 18.5 :
    print ("You are underweight. Watch your health.")
elif  18.5 <=  bmi <= 24.5:
    print("You are fit & healthy.")
else  :
    print("You are overwieght you need to work out more and watch your diet.")



