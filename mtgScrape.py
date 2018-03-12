#Card images are at: http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=430718&type=card
#The multiverseid= the cards id (i.e. 430718)
#Link below is for cards with images
#http://gatherer.wizards.com/Pages/Search/Default.aspx?output=standard&format=["Amonkhet+Block"]
from bs4 import BeautifulSoup
import requests, csv, pprint

def getFlavor(cardUrlId):
    cardUrl = requests.get(
    'http://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid='+ str(
    cardUrlId))
    soup = BeautifulSoup(cardUrl.text, 'html5lib')
    flavor = soup.select(".flavortextbox")
#   Instantiates list to be returned
    cardFlavor = []
    cardInfo = soup.select(".value")
#   Gets card name
    cardFlavor.append(cardInfo[1].string.strip())
#   Gets expansion set
    cardFlavor.append(cardInfo[8].a.find_next_sibling("a").string)
#   Gets flavor text and appends to cardFlavor list
    flavorText = []
    for text in flavor:
        flavorText.extend(text.string)
    return cardFlavor.append(flavorText)

getFlavor(3239)
