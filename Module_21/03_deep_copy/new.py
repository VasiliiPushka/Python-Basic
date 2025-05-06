import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на телефон',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def site_template(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = site_template(sub_struct, key, meaning)
            if result:
                return site

number_sites = int(input('Введите кол-во сайтов: '))
d_copy = dict()
goods = dict()
for _ in range(number_sites):
    product_name = input('Введите название продукта для нового сайта: ')
    key = {'title': f'Куплю/продам {product_name} недорого', 'h2' : f'У нас самая низкая цена на {product_name}'}
    for i in key:
        site_template(site, i, key[i])
    name_of_product = f'Сайт для {product_name}:'
    d_copy = copy.deepcopy(site)
    goods[name_of_product] = d_copy
    for key, value in goods.items():
        print(key)
        print(value)





