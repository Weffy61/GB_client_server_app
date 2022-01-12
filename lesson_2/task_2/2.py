import json


def write_order_to_json(item, quantity, price, buyer, date):
    info = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    # вам нужно подгрузить JSON-объект
    with open('order.json', encoding='UTF-8') as f_read:
        reader = json.load(f_read)
        # достучаться до списка, который и нужно пополнять
        orders = reader['orders']
        # добавляем info в список orders
        orders.append(info)

    with open('order.json', 'w', encoding='UTF-8') as f_write:
        json.dump(orders, f_write, indent=4)


write_order_to_json('printer', '10', '6700', 'Ivanov I.I.', '24.09.2017')
# write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
# write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
# write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')

