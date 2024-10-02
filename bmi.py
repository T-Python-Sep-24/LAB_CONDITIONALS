
weight=float(input("provide your wieght :"))
height=float(input("provide your height :"))

bmi:float = weight / (height ** 2)

if bmi>=25:
    print("You are overwieght you need to work out more and watch your diet.")
elif 18.5<= bmi<25:
    print("You are fit & healthy")
else:
    print("You are underweight. Watch your health.")