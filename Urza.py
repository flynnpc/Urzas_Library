from bs4 import BeautifulSoup
import requests, re
# update 01 - replaced if beautiful soup object present with try except AttributeError
# update 02 - replaced soup.text with soup.content to for easier use in Beautifulsoup
# update 03 - replaced int with float declaration in mana_cost_convert to account for unglued cards
# update 04 - updated expansion function to account for missing img
class UrzasPress:

    def __init__(self, cardUrlId):
        self.id = str(cardUrlId)
        self.win10Head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.cardUrl = requests.get(
        'http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid='+
        self.id, headers=self.win10Head, timeout=30)
        self.soup = BeautifulSoup(self.cardUrl.content,'lxml')
    def checkUrl(self):
        if self.soup.select('.introheader'):
            return False
        else:
            return True
    def card_name(self):
        try:
            self.name_div = self.soup.find("div", string=re.compile(
                                                        "Card Name:"))
            return self.name_div.find_next_sibling('div').get_text().strip()
        except AttributeError:
            return
    def mana_cost(self):
        try:
            self.mana_label = self.soup.find("div", string=re.compile(
                                                        "Mana Cost:"))
            self.mana_flash = self.mana_label.find_next_sibling(
                                            'div').find_all("img")
            self.mana_cost = [self.mana['alt'] for self.mana in self.mana_flash]
            return self.mana_cost
        except AttributeError:
            return
    def mana_cost_convert(self):
        try:
            self.converted_label = self.soup.find("div", string=re.compile(
                                                    "Converted Mana Cost:"))
            self.total_mana = self.converted_label.find_next_sibling(
                                            'div').get_text().strip()
            return float(self.total_mana)
        except AttributeError:
            return
    def card_type(self):
        try:
            self.type_label = self.soup.find("div", string=re.compile("Types:"))
            self.card_type = self.type_label.find_next_sibling(
                                        'div').get_text().strip()
            return self.card_type
        except AttributeError:
            return
    def card_text(self):
        try:
            self.text_div = self.soup.select(".cardtextbox")
            self.card_txt = []
            for self.flash_text_box in self.text_div:
                self.symbols = self.flash_text_box.find_all('img')
                self.alt_List = []
                for self.alt_flash in self.symbols:
                    self.alt_List.append(self.alt_flash['alt'])
                self.alt_List.append(self.flash_text_box.get_text().strip())
                self.card_txt.append(self.alt_List)
            return self.card_txt
        except AttributeError:
            return
    def flavor_text(self):
        try:
            self.flash_flavor_label = self.soup.select(".flavortextbox")
            self.flavor_txt = [self.line.get_text().strip()
                                        for self.line in self.flash_flavor_label]
            return self.flavor_txt
        except AttributeError:
            return
    def expansion(self):
        try:
            self.set_label = self.soup.find("div", string=re.compile(
                                    "Expansion:")).find_next_sibling()
            # self.expansion_set = self.set_label.img["title"]
            self.expansion_set = self.set_label.get_text().strip()
            return self.expansion_set
        except AttributeError:
            return
    def rarity(self):
        try:
            self.rarity_label = self.soup.find("div", string=re.compile(
                                                            "Rarity:"))
            self.rare = self.rarity_label.find_next_sibling(
                                        'div').get_text().strip()
            return self.rare
        except AttributeError:
            return
    def card_number(self):
        try:
            self.number_label = self.soup.find("div", string=re.compile(
                                                        "Card Number:"))
            self.number = self.number_label.find_next_sibling(
                                        'div').get_text().strip()
            return self.number
        except AttributeError:
            return
    def artist(self):
        try:
            self.artist_label = self.soup.find("div", string=re.compile(
                                                                "Artist:"))
            self.art = self.artist_label.find_next_sibling(
                                    'div').get_text().strip()
            return self.art
        except AttributeError:
            return
    
