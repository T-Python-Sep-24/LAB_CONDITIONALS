# Ask the user for their name
name = input("Please enter your name: ")

# Check if the name length is more than 2 characters
if len(name) <= 2:
    print("The name length must be more than 2 characters, please provide a valid name.")
else:
    # Ask the user for their email
    email = input("Please enter your email: ")

    # Check if the email is valid
    if '@gmail.com' in email and email.index('@') < email.index('.'):
        print(f"Welcome {name}, you registered with the email {email}!")
    else:
        print("The email is not valid, please provide a valid email.")