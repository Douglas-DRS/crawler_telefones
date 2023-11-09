import requests
from bs4 import BeautifulSoup


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


resposta = buscar(URL_AUTOMOVEIS)
if resposta:  
  soup = parsing(resposta)

  cards_pai = soup.find('div', class_='ui three doubling link cards')
  cards = cards_pai.find_all('a')
  print(cards)