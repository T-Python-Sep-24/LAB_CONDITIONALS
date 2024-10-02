# Bouns 2 for Lab 3         

#The User Input
userName = input("Please enter your Name: ")
userEmail = input("Please enter your Email: ")

#Check validation
if len(userName) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name.")

elif '@gmail.com' in userEmail and userEmail.endswith('@gmail.com'):
        print(f"Welcome, {userName}! you registered with the email {userEmail}!")

else:
     print(" the email is not valid , please provide a valid email.")

