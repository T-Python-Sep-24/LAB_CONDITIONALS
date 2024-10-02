movieTopGun :int = 3
popularityCore : float = 72.65

if movieTopGun >= 4 and popularityCore >80.0:
    print("Highly recommended")

elif movieTopGun >= 3 and popularityCore >= 72.65: 
    print("I recommended it . It is good") 

elif movieTopGun <=2 and popularityCore >= 60.0: 
    print("You should check it out!") 

else :
    print("Don't watch it. It is a waste of time")
