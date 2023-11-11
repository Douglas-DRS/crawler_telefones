import re

import requests
from bs4 import BeautifulSoup

DOMINIO = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOVEIS = 'https://django-anuncios.solyd.com.br/automoveis/'


def requisicao(url):
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
  try:
    cards_pai = soup.find('div', class_='ui three doubling link cards')
    cards = cards_pai.find_all('a')
  except:
    print("Erro ao encontrar links")
    return None

  links= []
  for card in cards:
    link = card['href']
    links.append(link)

  return links


def encontrar_telefone(soup):
  try:
    descricao = soup.find_all('div', class_='sixteen wide column')
  except:
    print('Erro ao encontrar descricao')
    return None
  
  regex = re.findall(r'\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})', str(descricao))
  print(regex)


resposta_busca = requisicao(URL_AUTOMOVEIS)
if resposta_busca:  
  soup = parsing(resposta_busca)
  if soup:
    links = encontrar_links(soup)
    resposta_anuncio = requisicao(DOMINIO + links[0])
    if resposta_anuncio:
      soup_anuncio = parsing(resposta_anuncio)
      if soup_anuncio:
        encontrar_telefone(soup_anuncio)