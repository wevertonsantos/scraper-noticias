from selenium import webdriver

# abrir o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://g1.globo.com/")

# colocar o navegador em tela cheia
navegador.maximize_window()

# selecionar um elemento na tela
noticias = navegador.find_elements("css selector", 'p[data-mrf-layout-title]')

dados_noticias = {}

for noticia in noticias:
    # armazenando notícias no dic
    dados_noticias[f"noticia_{noticias.index(noticia)}"] = noticia.text

with open("Principais notícias do dia.txt","w") as arquivo:
    for dado_noticia in dados_noticias:
        if dado_noticia == list(dados_noticias)[-1]:
            arquivo.write(f"{dado_noticia}:{dados_noticias[dado_noticia]}")
        else:
            arquivo.write(f"{dado_noticia}:{dados_noticias[dado_noticia]}\n")