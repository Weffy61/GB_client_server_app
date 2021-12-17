import chardet

with open('test_file.txt', 'rb') as f:
    for i in f:
        file = chardet.detect(i)
        i = i.decode(file['encoding']).encode('utf-8')
        print(type(i.decode('utf-8')))
