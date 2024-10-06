print('Write your weight please: ')
weight = input()
print('Write your height in cm please: ')
height = input()
print('')
bmi = int(weight) / ((int(height) / 100)**2)

if (bmi  >= 25) and (bmi <= 29.9):
    print('You are overwieght you need to work out more and watch your diet')
elif (bmi  >= 18.5) and (bmi <= 24.9):
    print('You are fit & healthy')
elif (bmi  < 18.5):
    print('You are underweight. Watch your health')
else:
    print('you are obese')