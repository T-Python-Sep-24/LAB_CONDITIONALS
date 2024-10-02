userNmae = input("Enter name : ")
userEmail = input ("Enter email: ")

if userNmae == "Ahmed" and userEmail == "ahmed@gmail.com":
    print(f"welcome Ahmed, you registered with the email ahmed@gmail.com !")

elif userEmail != "Ahmed" and userEmail != "ahmed@gmail.com" : 
    print("the email is not valid , please provide a valid email .")     

else: 
    print("the name length must be more than 2 characters, please provide a valid name.")