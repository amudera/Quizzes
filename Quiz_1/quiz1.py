from pprint import pprint

with open('currency.txt', 'r') as file_object:
        for line in file_object:
            splits = line.split()
            ccy = "symbol: " + list(splits)[0]
            rates = "rate: " + list(splits)[1]
            ccy1 = tuple([ccy])
            rates2 = tuple([rates])

currency_dict = dict(zip(ccy1,rates2))
pprint(currency_dict)

#currency_dict['symbol']: ccy
