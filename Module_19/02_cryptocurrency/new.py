data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

#Вывести списки ключей и значений словаря.
keys_dict = [data.keys()]
values_dict = [data.values()]
print(keys_dict)
print(values_dict, "\n")


#В “ETH” добавить ключ “total_diff” со значением 100.
data['ETH']['total_diff'] = 100
print(data['ETH'], "\n")


#Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
data['tokens'][0]['fst_token_info']['name'] = 'doge'
print(data['tokens'][0]['fst_token_info']['name'], '\n')


#Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
data['tokens'][0].pop('total_out')
data['ETH']['total_Out'] = 0
print(data['ETH']['total_Out'])


#Внутри "sec_token_info" изменить название ключа “price” на “total_price”.
data['tokens'][1]['sec_token_info'].pop('price')
data['tokens'][1]['sec_token_info']['total_price'] = False
print(data['tokens'][1]['sec_token_info'])