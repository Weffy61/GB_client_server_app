import yaml

info = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_quantity': 4,
    'items_price': {
                    'computer': '200€-1000€',
                    'printer': '100€-300€',
                    'keyboard': '5€-50€',
                    'mouse': '4€-7€'
    }
}
with open('file.yaml', 'w', encoding='UTF-8') as f:
    yaml.dump(info, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
with open('file.yaml', 'r', encoding='UTF-8') as f_new:
    compare = yaml.load(f_new, Loader=yaml.SafeLoader)

if compare == info:
    print('All is good')


