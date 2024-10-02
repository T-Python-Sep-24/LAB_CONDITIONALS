name:str = input("name: ")
email:str = input("email: ")
if len(name) > 2 :
    if email.endswith("@gmail.com"):
        print("welcome {}, you registered with the email {} !".format(name,email))
    else :
        print("the email is not valid , please provide a valid email .")
else:
    print("the name length must be more than 2 characters, please provide a valid name.")