# Faz scraping simples de um site e extrai títulos de artigos
# Requer: pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://blog.python.org/'
resposta = requests.get(url)

if resposta.status_code == 200:
    conteudo = BeautifulSoup(resposta.text, 'html.parser')
    titulos = conteudo.find_all('h3')  # h3 costuma conter títulos de postagens
    print("Títulos encontrados no blog:")
    for titulo in titulos:
        print("-", titulo.text.strip())
else:
    print("Erro ao acessar a página:", resposta.status_code)
