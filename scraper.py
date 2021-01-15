import requests
from bs4 import BeautifulSoup
from win32com.client import Dispatch

def scraper(url):

    body = BeautifulSoup(requests.get(url).content, 'html.parser').body

    correct_ul = list(body.find_all('ul'))[5]

    child = list(correct_ul.findChildren('li', recursive=False))[3]

    speak = Dispatch("SAPI.SpVoice")

    try:
        if(child['class'][0]=="validate"):
            speak.Speak("votre colis est arrivé")
    except KeyError:
        pass

mondial_relay_url = "https://www.mondialrelay.fr/suivi-de-colis/?NumeroExpedition=71063121&CodePostal=49100"
scraper(mondial_relay_url)
