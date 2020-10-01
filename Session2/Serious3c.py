n = int(input('Input a number: ')) + 1

j = 0
for i in range(1, n):
    j += 1
    for a in range(1, n):
        print(a * j, end= " ")
    print("")
    
    