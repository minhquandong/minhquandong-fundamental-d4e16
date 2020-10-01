n = int(input('Enter the total numbers of 1 and 0: ')) + 1

for i in range(1, n):
    j = i % 2
    if j != 0:
        print(1, end= " ")
    else:
        print(0, end= " ")