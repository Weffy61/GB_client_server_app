# В данном задании использовал часть ващего разбора, сам не смог разобрать полностью))

import csv
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    number = 1
    for file in file_list:
        with open(file, 'r') as f:
            for word in f:
                prod = re.search('Изготовитель системы: \s*\S*', word)
                name = re.search('Название ОС: \s*\S*\s*\S*\s*\S*', word)
                code = re.search('Код продукта: \s*\S*', word)
                base = re.search('Тип системы: \s*\S*', word)

                if prod is not None:
                    prod = prod.group().replace(' ', '')
                    space_cleaner_prod = re.split(r':', prod)
                    os_prod_list.append(space_cleaner_prod[1])

                if name is not None:
                    name = name.group()
                    space_cleaner_name = ' '.join((str(name)).split()).split(':')[1]
                    space_cleaner_name = space_cleaner_name.lstrip(' Microsoft ')
                    os_name_list.append(space_cleaner_name)

                if code is not None:
                    code = code.group().replace(' ', '')
                    space_cleaner_code = re.split(r':', code)
                    os_code_list.append(space_cleaner_code[1])

                if base is not None:
                    base = base.group().replace(' ', '')
                    base_cleaner = ' '.join((str(base)).split()).split(':')[1]
                    os_type_list.append(base_cleaner)

    for i in range(0, 3):
        data = []
        data.append(number)
        number += 1
        data.append(os_prod_list[i])
        data.append(os_name_list[i])
        data.append(os_code_list[i])
        data.append(os_type_list[i])
        main_data.append(data)
    return main_data


def write_to_csv():
    all_data = get_data()
    with open('data_report.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(('№', 'Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'))
        for data in all_data:
            writer.writerow(data)


write_to_csv()
