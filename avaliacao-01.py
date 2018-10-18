import requests
import requests_cache
import sys

from bs4 import BeautifulSoup
# from sklearn.naive_bayes import MultinomialNB
import pandas as pd

requests_cache.install_cache('demo_cache')


def download(url, num_retries=2):
    page = None
    try:
        response = requests.get(url)
        page = response.text
        if response.status_code >= 400:
            print('Download error:', response.text)
            if num_retries and 500 <= response.status_code < 600:
                return download(url, num_retries - 1)
    except requests.exceptions.RequestException as e:
        print('Download error:', e.reason)
    return page


url = 'http://www.tce.pi.gov.br'
html = download(url)
soup = BeautifulSoup(html, 'html.parser')

table = soup.find(attrs={'id': 'latestnews'})
_links = table.select('a.latestnews')

links = []
# print(_links)
for link in _links:
    row = {
        'html': download(link['href']),
        'titulo': link.text
    }
    links.append(row)


while True:
    index = 0
    for link in links:
        print(str(index) + ' - ' + link['titulo'] + '\n')
        index += 1

    option = input('Escolha uma das noticias, ou 5 para sair \n')

    # print(links[option]['html'])

    try:
        print(links[int(option)]['html'])
        x = input('Exibir o menu novamente? 1 para sim 5 para sair \n')
        if int(x) == 5:
            break
    except Exception:
        if int(option) == 5:
            break
        else:
            print('Opção invalida')


