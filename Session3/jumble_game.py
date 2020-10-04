import random

word_list = ['champion', 'question', 'document', 'module', 'navigation', 'huntress',
    'trichotillomania', 'psychotomimetic', 'incomprehensibilities ']

word = random.choice(word_list)     # chọn random 1 từ trong list
w_list = list(word)                 # chuyển từ str sang list
random.shuffle(w_list)
print(w_list)
count = 0
while count < 3:
    answer = input('Your answer: ')
    if answer != word:
        print('Oops, try again!')
        count += 1
    else:
        print('Correct!')
        break
print('Bye!')    