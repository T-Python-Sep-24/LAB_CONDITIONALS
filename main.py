# Movie Recommendation
movie = "Inception"
rating = 3
popularity = 72.65

if rating >= 4 and popularity > 80:
    print("Highly recommended")
elif rating >= 3 and popularity > 70:
    print("I recommend it. It is good")
elif rating <= 2 and popularity > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")

# Bonus 1: BMI Calculation
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif 18.5 <= bmi < 24.9:
    print("You are fit & healthy.")
else:
    print("You are overweight. You need to work out more and watch your diet.")

# Bonus 2: User Registration
name = input("Please enter your name: ")
email = input("Please enter your email: ")

if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
elif not email.endswith("@gmail.com"):
    print("The email is not valid, please provide a valid email.")
else:
    print(f"Welcome {name}, you registered with the email {email}!")
