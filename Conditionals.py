Movie = "Bad Boy"
MovieRate = 3
popularity = 72.65

if (MovieRate >= 4) and (popularity > 80):
    print('Highly recommended')
elif (MovieRate >= 3) and (popularity > 70):
    print('I recommended it . It is good')
elif (MovieRate <= 2) and (popularity > 60):
    print('You should check it out!')
else:
    print('Don\'t watch it. It is a waste of time')

