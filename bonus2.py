## Bonus 2
### write a program that asks the user to provide his name and his email using input , then do the following:
name : str = input("Write your name: ")
email : str = input("Write your gmail: ")

if len(name) <=2:
    print("the name length must be more than 2 characters, please provide a valid name.")

if ("@gmail.com") in email and email.endswith("@gmail.com"):
    print(f"Welcome {name} you registered with the email {email}")
else:
    print("the email is not valid , please provide a valid email .")
    
