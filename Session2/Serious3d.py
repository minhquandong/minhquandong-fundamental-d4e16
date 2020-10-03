n = int(input('Input a number: ')) + 1

for i in range(1, n):
    if (i % 2) != 0:
        for x in range(1, n):
            y = x % 2
            if y != 0:
                print(1, end= " ")
            else:
                print(0, end= " ")
    
    else:
        for x in range(1, n):
            y = x % 2
            if y == 0:
                print(1, end= " ")
            else:
                print(0, end= " ")
    
    print("")

    