user_input = input('Please input your name: ')
user_input = user_input.lower()
words = user_input.split()

while '\t' in words:
    del words[words.index('\t')]
    
while '' in words:
    del words[words.index('')]
    
# # Cách 1
# for i in range(len(words)):
#     item = words[i]
#     alphabet = list(item)
#     alphabet[0] = alphabet[0].upper()
#     words[i] = ''.join(alphabet)
# new_name = ' '.join(words)

# Cách 2
for i in range(len(words)):
    words[i] = words[i].capitalize()
new_name = ' '.join(words)

print('Standardized name:', new_name)