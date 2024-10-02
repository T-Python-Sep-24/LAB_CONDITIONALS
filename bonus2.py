'''
Asks the user to provide his name and his email using input , then do the following:
if the email is valid: display a welcome message 
if the email or name is not valid: please provide a valid email or
the name length must be more than 2 characters
'''

name: str = (input("Your name: "))
email: str = (input("Your email: ")).lower()

# Check if the name length is more than 2 characters.
isLengthValid = False
if len(name) > 2:
    isLengthValid = True

# Check if the email is valid (only accept @gmail.com)
isGmail = False
gmail: str = "@gmail.com"
if gmail in email:
    isGmail = True

# Check if the email and name length are valid:
if isLengthValid and isGmail:
    print(f"welcome {name}, you registered with the email {email} !")
elif not isGmail:
    print("the email is not valid , please provide a valid email")
else:
    print("the name length must be more than 2 characters, please provide a valid name.")
