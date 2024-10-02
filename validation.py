print ("\n––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
print ("\n Welcome to my Email Address Validator!")
print("\n Please input the name and email address that you would like to validate.")
print ("\n––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
name:str=input("Enter your name:")
email:str=input("Enter your email address:")


#Check that the name length is more than 2 characters.
if len(name)<=2:
    print("The name length must be more than 2 characters, please provide a valid name.")
# To check is exactly one @ symbol
elif email.count('@') != 1:
    print("The email is not valid , please provide a valid email .")
# To ensure email ends with @gmail.com
elif not email.endswith('@gmail.com'):
    print("The email is not valid , please provide a valid email .")
# To check if there is at least one character before the @
elif email.index('@') == 0:
        print("The email is not valid, please provide a valid email.")
# To check if there is at least one character after the @.
elif email.index('@') + 1 == len(email):
        print("The email is not valid, please provide a valid email.")
else:
    print(f"Welcome {name}, you registered with the email {email} !")