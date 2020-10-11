inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# add 'pocket' to the inventory
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)

# Remove 'dagger' from the list of items stored under the 'backpack' key
a = inventory['backpack'].pop(1)
inventory['pocket'].append(a)
print(inventory)

# Add 50 to the number stored under the 'gold' key
inventory['gold'] = inventory['gold'] + 50
print(inventory)