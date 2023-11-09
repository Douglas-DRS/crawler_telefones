import requests
from bs4 import BeautifulSoup

DOMINIO = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOVEIS = 'https://django-anuncios.solyd.com.br/automoveis/'


def buscar(url):
  try:
    resposta = requests.get(url)
    if resposta.status_code == 200:
      return resposta.text
    else:
      print('Erro ao fazer requisição')
  except Exception as error:
    print('Ocorreu um erro inesperado')
    print(error)


def parsing(resposta_html):
  try:
    soup = BeautifulSoup(resposta_html, 'html.parser')
    return soup
  except Exception as error:
    print('Erro ao fazer parsing do HTML')
    print(error)


def encontrar_links(soup):
  cards_pai = soup.find('div', class_='ui three doubling link cards')
  cards = cards_pai.find_all('a')

  links= []
  for card in cards:
    link = card['href']
    links.append(link)

  return links


resposta = buscar(URL_AUTOMOVEIS)
if resposta:  
  soup = parsing(resposta)
  if soup:
    links = encontrar_links(soup)
    print(links)