from random import choice
from random import randrange
from time import time as time_now
import string
import webbrowser
webbrowser.open('https://www.youtube.com/watch?v=1-AltLENQGg')
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
        direction = choice(['North', 'South', 'East', 'West'])
        now = str(time_now()) #Hoy many seconds passed since 1 January 1970
        adjective = choice(adjectives)
        noun = choice(nouns)
        number = randrange(0, 100)
        special_char = choice(string.punctuation)
        password = direction + now + adjective + noun + str(number) + special_char
        print('New password: %s' % password)
    response = input('Do you want to generate new passwords? Input yes/no: ')
    if response == 'no':
        break

