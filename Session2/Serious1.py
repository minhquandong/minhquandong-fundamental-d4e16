mass = float(input('Input your weight (kg)'))
height = float(input('Input your height (cm)')) / 100

bmi = mass / (height * height)

if bmi >= 30:
    print(bmi, '- Obese')
elif bmi >= 25 and bmi < 30:
    print(bmi, '- Overweight')
elif bmi >=18.5 and bmi < 25:
    print(bmi, '- Normal')
elif bmi >= 16 and bmi < 18.5:
    print(bmi, '- Underweight')
else:
    print(bmi, '- Severely')