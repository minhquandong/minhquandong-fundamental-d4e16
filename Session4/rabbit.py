def print_rabbit(i, j):
    return print('Month', i, ':', j, 'pair(s) of rabbit')

a1 = 0
a2 = 1
count = 0
month = 5
while count < month:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print_rabbit(count, a3)
    count +=1
