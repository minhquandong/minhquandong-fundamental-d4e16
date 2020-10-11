numbers = [1, 6, 8, 1, 2, 1, 5, 6]
choice = int(input('Enter a number? '))


# with count() function
count = numbers.count(choice)
if count > 1:
    print(choice, 'appears', count, 'times in my list')
else:
    print(choice, 'appears', count, 'time in my list')

# without count() function
total = 0
for i in range(len(numbers)):
    if choice == numbers[i]:
        total += 1
if total > 1:
    print(choice, 'appears', total, 'times in my list')
else:
    print(choice, 'appears', total, 'time in my list')

