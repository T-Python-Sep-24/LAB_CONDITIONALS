movie="forrest gump"
rating:int=2
score:float=49

if rating>=4 and score>80:
    print("Highly recommended")
elif rating>=3 and score>70:
    print("i recommended it .it is good")
elif rating<=2 and score>60:
    print("you should check it out!")
else:
    print("Don't watch it. It is a waste of time")