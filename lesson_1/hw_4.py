words = ['разработка', 'администрирование', 'protocol', 'standard']
encoded_words = []
decoded_words = []

for word in words:
    i = word.encode('utf-8')
    encoded_words.append(i)

for encode in encoded_words:
    n = encode.decode('utf-8')
    decoded_words.append(n)

print(f'{encoded_words}, \n{decoded_words}')
