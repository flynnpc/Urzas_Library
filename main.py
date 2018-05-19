from bs4 import BeautifulSoup
from Urza import UrzasPress
import requests, re, csv, os
# Alpha 1,295
# Beta 296,597
# Unlimited 598,899
# Arabian Nights 900,991
# Antiquities 992,1091
# Revised 1092,1397
# Legends 1398,1707
# The Dark 1708,1826
# Fallen Empires 1827,2013
# Fourth ed 2014,2391
# Ice Age 2392,2774
# Dominaria 442889, 443152
set_list = os.path.join(os.path.dirname(__file__), "all.csv")

with open(set_list, 'w', newline='') as csvfile:
    fields = ['card_name','mana_cost','mana_total','card_type','card_text',
    'flavor_text', 'card_set', 'rarity','card_number' ]
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    for card in range(1,443152):
        uz = UrzasPress(card)
        writer.writerow({'card_name':uz.card_name(),
                        'mana_cost': uz.mana_cost(),
                        'mana_total':uz.mana_cost_convert(),
                        'card_type':uz.card_type(),
                        'card_text':uz.card_text(),
                        'flavor_text':uz.flavor_text(),
                        'card_set':uz.expansion(),
                        'rarity':uz.rarity(),
                        'card_number':uz.card_number()})
