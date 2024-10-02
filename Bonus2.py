name = str(input("user name : "))
email = str(input("user email : "))


if len(name) > 2 and  "@gmail" in email: 
    print("welcome {} , you registered with the email : {}".format(name,email))
elif len(name) <=2 :
       print("the name length must be more than 2 characters, please provide a valid name.")
else:
    print("the email is not valid , please provide a valid email")


