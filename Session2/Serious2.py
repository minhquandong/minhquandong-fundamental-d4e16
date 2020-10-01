n = int(input('Please input a number:'))

while True:
    f = 1
    for i in range(2, n + 1):
        f = f * i
        print('Factorial =', f)
    break
    