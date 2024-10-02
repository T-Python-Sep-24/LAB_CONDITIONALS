#Ask user for their name
name: str = input("Please enter your name: ")

#Ask user for their email
email: str = input("Please enter your email: ")

#Check for email and name validity
if len(name) < 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
elif not email.endswith("@gmail.com"):
    print("The email is not valid, please provide a valid email.")
else: 
    print(f"Welcome {name}, you registered with the email {email}")