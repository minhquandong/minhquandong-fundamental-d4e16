user_input = input('Please input your name: ')
user_input = user_input.lower()
# print(user_input)
words = user_input.split()

while '\t' in words:
    del words[words.index('\t')]
    
while '' in words:
    del words[words.index('')]
    
# print(words)

for i in range(len(words)):
    item = words[i]
    alphabet = list(item)
    alphabet[0] = alphabet[0].upper()
    # print(alphabet)
    words[i] = ''.join(alphabet)
    # print(words)
new_name = ' '.join(words)
print('Standardized name:', new_name)