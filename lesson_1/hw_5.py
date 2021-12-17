import subprocess
import chardet


def stdout(ping_name):
    count = 0
    for i in ping_name.stdout:
        result = chardet.detect(i)
        i = i.decode(result['encoding']).encode('utf-8')
        print(i.decode('utf-8'))
        count += 1
        if count > 4:
            break


args_1 = ['ping', 'yandex.ru']
args_2 = ['ping', 'youtube.com']

ping_1 = subprocess.Popen(args_1, stdout=subprocess.PIPE)
ping_2 = subprocess.Popen(args_2, stdout=subprocess.PIPE)

stdout(ping_1)
stdout(ping_2)
