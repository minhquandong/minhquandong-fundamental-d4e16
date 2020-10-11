sheeps = [5, 7, 300, 90, 24, 50, 75]
months = [1, 2, 3, 4]

# 2.3 - sheer the biggest sheep and return it to 8
big_sheep = max(sheeps)
sheeps[sheeps.index(big_sheep)] = 8
print('After sheering, here is my flock:')
print(sheeps)

# # Cách 2:
# max_number = sheeps[0]
# for sheep in sheeps:
#     if max_number < sheep:
#         max_number = sheep
# print(max_number)


# 2.4 - sheeps have increased their size
new_flock = sheeps[:]
for (i, v) in enumerate(new_flock):
    new_flock[i] = v + 50
print('One month has passed, now here is my flock:')
print(new_flock)


# 2.5 - months has passed
count = 0
while count < len(months):
    for i in months:
        new_flock = sheeps[:]
        for (j, v) in enumerate(new_flock):
            new_flock[j] = v + 50 * i
        count += 1
        if i > 1:
            print(i, 'months has passed, now here is my flock')
        else:
            print(i, 'month has passed, now here is my flock')
        print(new_flock)
        