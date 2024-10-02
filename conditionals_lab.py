
movie = "Die Hard"
rating = 3  # out of 5
popularity_score = 72.66  # out of 100


if rating >= 4 and popularity_score > 80:
    print("It is Highly Recommended")
elif rating >= 3 and popularity_score > 70:
    print("I Recommend it, it is good :) ")
elif rating <= 2 and popularity_score > 60:
    print("your should check it out !!")
elif rating <= 2 and popularity_score < 50:
    print("I'd rather sleep than watch this movie, it is a waste of time ;| ")
