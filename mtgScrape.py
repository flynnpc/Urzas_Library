#Card images are at: http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=430718&type=card
#The multiverseid= the cards id (i.e. 430718)
#Link below is for cards with images
#http://gatherer.wizards.com/Pages/Search/Default.aspx?output=standard&format=["Amonkhet+Block"]
from bs4 import BeautifulSoup
import requests, csv, pprint, re
#http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=189875
def getFlavor(cardUrlId):
    cardUrl = requests.get(
    'http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid='+ str(
    cardUrlId))
    soup = BeautifulSoup(cardUrl.text,'lxml')
#Card name
    card_label = soup.find("div", string=re.compile("Card Name:"))
    card_name = card_label.find_next_sibling('div').get_text().strip()
#Mana Cost
    mana_label = soup.find("div", string=re.compile("Mana Cost:"))
    mana_symbols = mana_label.find_next_sibling('div').find_all("img")
    mana_cost = [mana['alt'] for mana in mana_symbols]
# Converted mana Cost
    converted_label = soup.find("div", string=re.compile("Converted Mana Cost:"))
    total_mana = converted_label.find_next_sibling('div').get_text().strip()
# type
    type_label = soup.find("div", string=re.compile("Types:"))
    card_type = type_label.find_next_sibling('div').get_text().strip()
# card text
    text_label = soup.select(".cardtextbox")
    card_text = [text.get_text() for text in text_label]
# flavor text
    flavor_label = soup.select(".flavortextbox")
    flavor_text = [line.get_text().strip() for line in flavor_label]
# expansion
    set_label = soup.find("div", string=re.compile("Expansion:")).find_next_sibling()
    expansion_set = set_label.img["title"]
    print(expansion_set)
# Rarity
    rarity_label = soup.find("div", string=re.compile("Rarity:"))
    rarity = rarity_label.find_next_sibling('div').get_text() #use get_text in other areas where you use .string
# Card Number
    number_label = soup.find("div", string=re.compile("Card Number:"))
    card_number = number_label.find_next_sibling('div').get_text().strip()
# Artist
    artist_label = soup.find("div", string=re.compile("Artist:"))
    artist = artist_label.find_next_sibling('div').get_text().strip()


getFlavor(4571)
