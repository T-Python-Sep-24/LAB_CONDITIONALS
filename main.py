#LAB_CONDITIONALS
movie:str="officer black belt"
rate:int=3
popularityscore:float=72.65
if rate >= 4 and popularityscore > 80:
    print("Highly recommended")
elif rate >= 3 and popularityscore > 70:
    print("I recommended it . It is good")
elif rate <= 2 and popularityscore > 60:
    print("You should check it out!")
else :
    print("Don't watch it. It is a waste of time")
print("-"*15)
#Bonus 1
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
BMI= weight/(height / 100)**2
print(f"Your BMI is {BMI} ")
if BMI >= 29.9:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI <=24.9:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")

#Bouns 2
print("-"*15)
username:str= input("Please enter your username: ")
Email:str= input("Please enter your Email: ")
if len(username)>=2 and Email.endswith("@gmail.com"):
     print(f"welcome {username} , you registered with the email {Email}")
else:
    print("the name length must be more than 2 characters, please provide a valid name.")
    print("the email is not valid , please provide a valid email .")