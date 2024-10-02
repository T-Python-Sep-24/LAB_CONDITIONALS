
movie:str = "John Wick"
movieRating:int = 3
popularity:float =72.65

if movieRating >= 4 and popularity > 80:
    print("Highly recommended")
elif movieRating >= 3 and popularity > 70:
    print("I recommended it . It is good")
elif movieRating <= 2 and popularity > 60:
    print("You should check it out!")
elif movieRating <= 2 and popularity < 50:
    print("Don't watch it. It is a waste of time")
