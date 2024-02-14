import subprocess
import os
from deep_translator import GoogleTranslator

# Idiomas mais falados na internet (em ordem de uso), removendo duplicatas
languages = ['en', 'es', 'pt', 'hi', 'ar', 'fr', 'ru', 'de', 'zh-CN', 'ja', 'ko', 'it', 'tr', 'nl', 'sv', 'pl', 'th', 'vi', 'el', 'tl', 'id', 'sw', 'ur']

# Pede ao usuário que insira uma frase para ser traduzida
phrase = input("Insira a frase para ser traduzida: ")

if phrase =="":
    print("Informe uma frase.")
    exit()  
# Pede ao usuário para escolher o mecanismo de busca (yt, bg ou tktk)
search_engine = input("Escolha o mecanismo de busca (yt, bg ou tktk): ")

valid_engines = ['yt', 'bg', 'tktk']
if search_engine not in valid_engines:
    print("Mecanismo de busca inválido.")
    exit()  

# Define o caminho do navegador com base no sistema operacional
if os.name == 'posix':  # MacOS
    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
elif os.name == 'nt':  # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
else:
    print("Navegador não suportado.")
    exit()

# Função para construir a URL com base no mecanismo de busca escolhido
def build_search_url(search_engine, translation):
    if search_engine == "yt":
        return f"https://www.youtube.com/results?search_query={translation.replace(' ', '+')}"
    elif search_engine == "bg":
         return f"https://www.bing.com/videos/search?q={translation.replace(' ', '+')}&go=Pesquisar&qs=ds&form=QBVR"
    elif search_engine == "tktk":
        return f"https://www.tiktok.com/tag/{translation.replace(' ', '-')}"

# Define uma variável dummy para filter_option, se necessário
filter_option = None

# Abre uma aba do navegador para cada idioma, mas limita a execução para evitar sobrecarga
for language in languages: 
    translation = GoogleTranslator(source='auto', target=language).translate(phrase)
    url = build_search_url(search_engine, translation)
    subprocess.run([chrome_path, url])
