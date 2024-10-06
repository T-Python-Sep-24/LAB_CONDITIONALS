height = 175.5
weight = 60

# kg/m²
bmi = weight / ((height / 100) ** 2)

print("Your BMI is:".format(bmi))

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif 18.5 <= bmi < 24.9:
    print("You are fit & healthy.")
elif bmi >= 25:
    print("You are overweight. You need to work out more and watch your diet.")


