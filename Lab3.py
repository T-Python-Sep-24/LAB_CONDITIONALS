#Lab 3

#The informations
myMovie:str = "The Avengers"
myMovieRate:int = 3
myMoviePopu:int = 72.65


#if statments
if myMovieRate >= 4 and myMoviePopu > 80:
    print("Highly Recommended")

elif myMovieRate >= 3 and myMoviePopu > 70:
    print("I Recommended it. It is Good")

elif myMovieRate <= 2 and myMoviePopu > 60:
    print("You Should Check it Out!")

else:
    print("Don't Watch it. It is a Waste of Time")   