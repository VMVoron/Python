print('Тест "Животные"')
score = 0
def check_guess(quess, answer):
    global score, guess
    still_guessing = True
    attempt = 0
    while (still_guessing == True) and (attempt < 3):
        if guess.lower() == answer.lower():
            print('Ответ верный!')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 3:
                guess = input('Ответ неверный. Попробуйте ещё раз. ')
            attempt +=1
    if attempt == 3:
        print('Правильный ответ: ' + answer)
guess = input('Какое из этих животных рыба? \n \
1) Кит \n 2) Дельфин \n 3) Акула \n 4) Кальмар \n \
Введите 1, 2, 3 или 4. ')
check_guess(guess, '3')
guess = input('Мыши - это млекопитающие. Да или нет? ')
check_guess(guess,'Да')
guess = input('Какой медведь живёт за полярным кругом? ')
check_guess(guess, 'белый медведь')
guess = input('Какое сухопутное животное самое быстрое? ')
check_guess(guess, 'гепард')
guess = input('Какое животное самое большое? ')
check_guess(guess, 'синий кит')
print('Вы набрали очков:' + str(score))
