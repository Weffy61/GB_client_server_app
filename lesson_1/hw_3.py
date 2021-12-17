words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        print(bytes(word, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово {word} невозможно записать')
