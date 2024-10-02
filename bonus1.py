weight = float(input("weight in KG: "))
height_cm = float(input("Height in CM: "))
height_m = height_cm / 100 
bmi : float = weight/height_m ** 2

print(f"Your BMI is{bmi: .2f}")
if bmi < 18.5 :
    print("You are underweight. Watch your health")

elif 18.5 <= bmi <= 24.9:
    print("You are fit & healthy")
    
else:
    print("You are overwieght you need to work out more and watch your diet")