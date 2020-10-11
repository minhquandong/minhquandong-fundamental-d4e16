a1 = 0
a2 = 1
count = 0

while count < 5:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    print('Month', count, ':', a3, 'pair(s) of rabbit')
    count +=1
