import requests
from bs4 import BeautifulSoup

URL = 'https://www.actirovkanorilsk.ru/'


def info_pars():
    act = []
    weather = ''
    roadsys = ''

    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'lxml')
    item = soup.select('#table')
    item1 = soup.select('#pogoda')
    item2 = soup.select('#doroga')

    for i in range(1):
        act = item[i].text.split('\n')
        weather = item1[i].text.lstrip()
        roadsys = item2[i].text[:-11:].lstrip()

    for i in range(12):
        act.remove('')

    for i in range(len(act)):
        if '&nbsp' in act[i]:
            act[i] = act[i].replace('&nbsp', ' ', 1)

    return act, weather, roadsys
