movie_name = "Inception"
movie_rating = 3
popularity_score = 72.65

if movie_rating >= 4 and popularity_score > 80:
    print("Highly recommended")
elif movie_rating >= 3 and popularity_score > 70:
    print("I recommend it. It is good")
elif movie_rating <= 2 and popularity_score > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight. Take care of your health.")
elif 18.5 <= bmi < 24.9:
    print("You are healthy and fit.")
else:
    print("You are overweight. Consider exercising and watching your diet.")

user_name = input("Enter your name: ")
user_email = input("Enter your email: ")

if len(user_name) <= 2:
    print("The name must be longer than 2 characters. Please enter a valid name.")
elif not user_email.endswith("@gmail.com"):
    print("Invalid email. Please provide a valid Gmail address.")
else:
    print(f"Welcome {user_name}, you registered with the email {user_email}!")
