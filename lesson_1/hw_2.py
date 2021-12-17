words = ['class', 'function', 'method']
bytes_list = []
for word in words:
    bytes_list.append(bytes(word, 'ascii'))

for i in bytes_list:
    print(f'{i} - {type(i)} - {len(i)}')
