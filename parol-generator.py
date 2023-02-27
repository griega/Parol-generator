import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
unusual_symbols = 'il1Lo0O'

chars = ''

while True:
    # Запросить у пользователя количество паролей для генерации
    try:
        kolpass = int(input('Сколько паролей необходимо? '))
    except ValueError:
        print('Введите число')
        continue

    # Спросите пользователя, какие наборы символов включить
    if input('Включать цифры 0123456789? Да/нет ') in {'Да', 'да'}:
        chars += digits
    if input('Включать прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Да/нет ') in {'Да', 'да'}:
        chars += uppercase_letters
    if input('Включать строчные буквы abcdefghijklmnopqrstuvwxyz? Да/нет ') in {'Да', 'да'}:
        chars += lowercase_letters
    if input('Включать ли символы !#$%&*+-=?@^_? Да/нет ') in {'Да', 'да'}:
        chars += punctuation
    if input('Включать необычные символы il1Lo0O? Да/нет ') in {'Да', 'да'}:
        chars += unusual_symbols

    # Спросите пользователя о длине паролей
    try:
        length = int(input('Какой длины должен быть пароль? '))
    except ValueError:
        print('Введите число')
        continue

    # Сгенерируйте пароли
    passwords = []
    for i in range(kolpass):
        password = ''.join([random.choice(chars) for i in range(length)])
        passwords.append(password)

    # Вывести пароли
    print('\n'.join(passwords))








