words = ['разработка', 'сокет', 'декоратор']
encodes = []
for word in words:
    print(f'{word} - {type(word)}')

for encode_word in words:
    i = encode_word.encode('utf-8')
    encodes.append(i)

for encode in encodes:
    print(f'{encode} - {type(encode)}')

