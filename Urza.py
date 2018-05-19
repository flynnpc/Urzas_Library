from bs4 import BeautifulSoup
import requests, re

class UrzasPress:

    def __init__(self, cardUrlId):
        self.id = str(cardUrlId)
        self.cardUrl = requests.get(
        'http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid='+
        self.id)
        self.soup = BeautifulSoup(self.cardUrl.text,'lxml')
    def card_name(self):
        if self.soup.find("div", string=re.compile("Card Name:")):
            self.card_label = self.soup.find("div", string=re.compile(
                                                        "Card Name:"))
            return self.card_label.find_next_sibling('div').get_text().strip()
        return
    def mana_cost(self):
        if self.soup.find("div", string=re.compile("Mana Cost:")):
            self.mana_label = self.soup.find("div", string=re.compile(
                                                        "Mana Cost:"))
            self.mana_symbols = self.mana_label.find_next_sibling(
                                            'div').find_all("img")
            self.mana_cost = [mana['alt'] for mana in self.mana_symbols]
            return self.mana_cost
        return
    def mana_cost_convert(self):
        if self.soup.find("div", string=re.compile("Converted Mana Cost:")):
            self.converted_label = self.soup.find("div", string=re.compile(
                                                    "Converted Mana Cost:"))
            self.total_mana = self.converted_label.find_next_sibling(
                                            'div').get_text().strip()
            return int(self.total_mana)
        return
    def card_type(self):
        if self.soup.find("div", string=re.compile("Types:")):
            self.type_label = self.soup.find("div", string=re.compile("Types:"))
            self.card_type = self.type_label.find_next_sibling(
                                        'div').get_text().strip()
            return self.card_type
        return
    def card_text(self):
        if self.soup.select(".cardtextbox"):
            self.text_label = self.soup.select(".cardtextbox")
            self.card_txt = []
            for self.text_box in self.text_label:
                self.symbols = self.text_box.find_all('img')
                self.alt_List = []
                for self.alt_text in self.symbols:
                    self.alt_List.append(self.alt_text['alt'])
                self.alt_List.append(self.text_box.get_text().strip())
                self.card_txt.append(self.alt_List)
            return self.card_txt
    def flavor_text(self):
        if self.soup.select(".flavortextbox"):
            self.flavor_label = self.soup.select(".flavortextbox")
            self.flavor_txt = [line.get_text().strip() for line in self.flavor_label]
            return self.flavor_txt
        return
    def expansion(self):
        if self.soup.find("div", string=re.compile(
                "Expansion:")).find_next_sibling():
            self.set_label = self.soup.find("div", string=re.compile(
                                    "Expansion:")).find_next_sibling()
            self.expansion_set = self.set_label.img["title"]
            return self.expansion_set
        return
    def rarity(self):
        if self.soup.find("div", string=re.compile("Rarity:")):
            self.rarity_label = self.soup.find("div", string=re.compile(
                                                            "Rarity:"))
            self.rare = self.rarity_label.find_next_sibling('div').get_text()
            return self.rare
        return
    def card_number(self):
        if self.soup.find("div", string=re.compile("Card Number:")):
            self.number_label = self.soup.find("div", string=re.compile(
                                                        "Card Number:"))
            self.number = self.number_label.find_next_sibling(
                                        'div').get_text().strip()
            return self.number
        return
    def artist(self):
        if self.soup.find("div", string=re.compile("Artist:")):
            self.artist_label = self.soup.find("div", string=re.compile(
                                                                "Artist:"))
            self.art = self.artist_label.find_next_sibling(
                                    'div').get_text().strip()
            return self.art
        return
