import subprocess
import os
from deep_translator import GoogleTranslator

# Idiomas mais falados na internet (em ordem de uso)
languages = ['en', 'es', 'pt', 'hi', 'ar', 'fr', 'ru', 'de', 'zh-CN', 'ja', 'ko', 'it', 'tr', 'nl', 'sv', 'pl', 'th', 'vi', 'el', 'tl', 'id', 'sw', 'ur', 'it', 'ko']

# Pede ao usuário que insira uma frase para ser traduzida
phrase = input("Insira a frase para ser traduzida: ")

# Pede ao usuário para escolher o mecanismo de busca (yt, bg ou tktk)
search_engine = input("Escolha o mecanismo de busca (yt, bg ou tktk): ")

# Verifica qual navegador está sendo utilizado para abrir o link
if os.name == 'posix':  # Unix/Linux/MacOS
    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
elif os.name == 'nt':  # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
else:
    print("Navegador não suportado.")

# Função para construir a URL com base no mecanismo de busca escolhido
def build_search_url(search_engine, translation, filter_option):
    if search_engine == "yt":
        return f"https://www.youtube.com/results?search_query={translation.replace(' ', '+')}"
    elif search_engine == "bg":
         return f"https://www.bing.com/videos/search?q={translation.replace(' ', '+')}&go=Pesquisar&qs=ds&form=QBVR"
    elif search_engine == "tktk":
        return f"https://www.tiktok.com/tag/{translation.replace(' ', '-')}"

# Faz a tradução da frase para cada um dos idiomas
for language in languages:

    # Faz a tradução
    translation = GoogleTranslator(source='auto', target=language).translate(phrase)

    # Cria a URL de pesquisa com base no mecanismo de busca escolhido
    url = build_search_url(search_engine, translation, filter_option)

    subprocess.run([chrome_path, url])

