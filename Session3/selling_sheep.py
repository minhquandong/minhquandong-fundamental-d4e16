sheeps = [5, 7, 300, 90, 24, 50, 75]
months = [1, 2, 3]

count = 0
while (count < len(months)):
    for i in months:
        
        # # Cách 1: clone sang list mới rồi x2 element trong list mới
        # new_flock = sheeps[:]
        # for (j, v) in enumerate(new_flock):
        #     new_flock[j] = v + 50 * i
        # count += 1

        # Cách 2: x2 element rồi gán vào 1 list mới
        new_flock = []
        for j in sheeps:
            new_value = j + 50 * i
            new_flock.append(new_value)
        count += 1
        
        if i > 1:
            print(i, 'months has passed, now here is my flock')
        else:
            print(i, 'month has passed, now here is my flock')
        print(new_flock)
        print('Now my biggest sheep has size', max(new_flock), 'let\'s sheer it')
        a = new_flock.index(max(new_flock))
        new_flock[a] = 8
        print('After sheering, here is my flock')
        print(new_flock)
        print('-----')

# tính total của flock hiện tại
total = sum(new_flock)
print('My flock has size in total:', total)
print('I would get', total, '* 2$ =', total * 2, '$')