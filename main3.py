name1=input("enter your name:")
email1=input("enter your email:")
if len(name1)>3 and email1.endswith("gmail.com"):
    print("welcome Ahmed, you registered with the email ahmed@gmail.com !")
elif len(name1)<3:
    print("the name length must be more than 2 characters, please provide a valid name.")
else:
    print("the email is not valid , please provide a valid email .")