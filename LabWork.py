#Movie name 
movName: str = "Skyscraper"

#Movie rating out of 5
movRating: int = 3

#Movie popularity out of 100 
movPopularity: float = 72.65

#Recommendation conditions 
if movRating >= 4 and movPopularity >= 80:
    print("Highly recommended")
elif movRating >=3 and movPopularity >=70:
    print("I recommend it, It is good")
elif movRating <= 2 and movPopularity >= 60:
    print("You should check it out!")
else: 
    print("Don't watch it. It is a waste of time.")
