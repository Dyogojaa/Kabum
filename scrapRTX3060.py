#Importação das Classes
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pandas as pd
import re



#Declarando Variaveis Cards
cards = []
card = {}



pesquisa = input("Digite o Produto:").replace(" ", "+")


print(pesquisa)
paginas = int(input("Digite o Número de Paginas a Pesquisa:"))


for i in range(paginas):

     #Obtendo o HTML
     response = urlopen('https://www.kabum.com.br/busca?query='+ pesquisa +'&page_number='+ str(i))
     html = response.read().decode('utf-8')
     soup = BeautifulSoup(html, 'html.parser')
     anuncios = soup.findAll("div", {"class": "productCard"})

     #print(anuncios)

     for anuncio in anuncios:
          card = {}

          # Nome
          card['Descricao'] = anuncio.find('h2', {'class': 'nameCard'}).getText()

          #Valor
          card['Valor'] = anuncio.find('span', {'class': 'priceCard'}).getText().replace("R$","").split()

          # # Imagens
          # image = anuncio.find('img', {'class': 'imageCard'})  #Pega a Imagem
          # image = image.get('src')  #Pega o Link
          # filename = image.split('/')[-1]  #Pega o Novo
          # urlretrieve(image, "./output/img/" + filename)

          cards.append(card)


# #Criando um DataFrame com os Resultados
dataset = pd.DataFrame(cards)
dataset.to_csv('./output/data/dataset.csv', sep=';', index=False, encoding='utf-8-sig')

