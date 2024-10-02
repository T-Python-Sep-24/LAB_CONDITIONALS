'''
## Bonus 2
### write a program that asks the user to provide his name and his email using input , then do the following:
- Check that the name length is more than 2 characters.
- Check that the email is valid (using string operations and coditionals)
- You only accept @gmail emails . 
- if the email is valid, display a welcome message to the user . for example :
```
welcome Ahmed, you registered with the email ahmed@gmail.com !

```
- if the email or name is not valid, display the message : 
```
 the email is not valid , please provide a valid email .
```

or 

```
the name length must be more than 2 characters, please provide a valid name.
```

### Note: don't use regular expressions or a library yet.
'''
username:str=input("Write  a name that has more than 2 characters: ").strip()
username
email:str=input("Write a Gmail email: ")
email_check="@gmail.com"
check=True
if email_check not in email:
    print("the email is not valid , please provide a valid email.")
    check=False
if len(username)<=2:
    print("the name length must be more than 2 characters, please provide a valid name.")
    check=False
if check:

    print(f"Welcome {username} you registered with the email {email} ! ")
