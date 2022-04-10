import random
import string
adjectives = ['sleepy', 'slow', 'hot',
              'cold', 'big', 'red',
              'orange', 'yellow', 'green',
              'blue', 'good', 'old',
              'white', 'free', 'brave', 'hairy']
nouns = ['apple', 'dinosaur', 'ball',
       'cat', 'goat', 'dragon',
       'car', 'duck', 'panda',
        'telephone', 'banana', 'teacher']
print('Welcome!')
while True:
    for num in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        password = adjective + noun + str(number) + special_char
        print('New password: %s' % password)
    response = input('Do you want to generate new passwords? Input yes/no: ')
    if response == 'no':
        break
