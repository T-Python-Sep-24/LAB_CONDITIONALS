import sys  # Just to break from the nested while loops

while True:
    name = input("Enter Your Name: ")

    if len(name) <= 2:
        print("The name length must be more than 2 characters, please provide a valid name.")
        print("Please try again with a valid name.")

    else:
        while True:
            email = input("Enter your Email: ")

            if not email.endswith("@gmail.com"):
                print(" the email is not valid , please provide a valid email.")

            else:
                print(" >>> WELCOME " + name + ", you registered with the email " + email + " <<<")
                sys.exit()
