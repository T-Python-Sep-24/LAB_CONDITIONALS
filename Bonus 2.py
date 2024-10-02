username=input("username :")
email=input("email :")
if len(username)<=2:
    print("the name length must be more than 2 characters, please provide a valid name.")
elif '@gmail.com' not in email:
    print("the email is not valid , please provide a valid email")
else:
    print(f"welcome {username},you registered with the email{email}")

