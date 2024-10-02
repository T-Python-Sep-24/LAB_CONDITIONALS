'''
## Bonus 2
'''

username=input("Enter your name: ")
email_address=input("Enter your Gamil E-mail: ")

if len(username)>2 and email_address.find("@gmail")>0:
    print(f"welcome {username}, you registered with the email {email_address} !")
else:
    if  len(username)<=2 and email_address.find("@gmail")==-1 :
         print("the email is not valid , please provide a valid email.")
         print("the name length must be more than 2 characters, please provide a valid name.")
    elif  email_address.find("@gmail")==-1:
        print("the email is not valid , please provide a valid email.")
    else:
        print("the name length must be more than 2 characters, please provide a valid name.") 
    