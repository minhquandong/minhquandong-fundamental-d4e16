prices = {
    'banana' : 4,
    'apple' : 2,
    'orange' : 1.5,
    'pear' : 3
}
stock = {}

# Put values in stock:
stock['banana'] = (6)
stock['apple'] = (0)
stock['orange'] = (32)
stock['pear'] = (15)

# For each key, print out the its price and stock information
for key in prices:
    print(key)
    print('Price:', prices[key])
    print('Stock:', stock[key])

# Total money
total = 0
for key in prices:
    total += prices[key] * stock[key]

print('Total money:', total)