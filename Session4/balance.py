balance = list(input('Please enter your balance: '))

while True:
    if balance[0] == '0':
        del balance[0]
    else:
        break

for i in range(len(balance), 0, -3):
    if i == len(balance):
        continue
    else:
        balance.insert(i, '.')
balance.insert(0, '$')
new_balance = ''.join(balance)

print('Your updated balance:', new_balance)