from selenium import webdriver

# abrir o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://g1.globo.com/")

# colocar o navegador em tela cheia
navegador.maximize_window()

# selecionar um elemento na tela
noticias = navegador.find_elements("css selector", 'p[data-mrf-layout-title]')

for noticia in noticias:
    print(noticia.text)