n = int(input('Input a number: ')) + 1

for i in range(1, n):
    for a in range(1, n):
        if a*i > 9:
            print(a * i, end= " ")
        else:
            print(a * i, end= "  ")
    print("")
    
# Cach 2 print hang ngang theo dang str
# for y in range(1, n):
#     str_x = ''
#     for x in range(1, n):
#         if x*y > 9:
#             str_x += str(x*y) + ' '
#         else:
#             str_x += str(x*y) + '  '
#     print(str_x)