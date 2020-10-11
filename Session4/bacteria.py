bacteria = int(input('How many B bacteria are there? '))
times = int(input('How much times in minutes will we wait? '))

result =  bacteria * 2 ** int((times / 2))

print('After', times, 'minutes, we would have', result, 'bacterias')
