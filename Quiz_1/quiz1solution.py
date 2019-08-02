from pprint import pprint

with open ('currency.txt','r') as f:
    txt = f.readlines()

def make_list(txt):
    currency_list = []
    for line in txt:
        currency_dict = {}
        line = line.split()
        currency_dict["Symbols: "] = line[0]
        currency_dict["Rates: "] = float(line[1])
        currency_list.append(currency_dict)
    return currency_list

pprint(make_list(txt))


