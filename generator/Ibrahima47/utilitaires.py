import requests
import json
from bs4 import BeautifulSoup

# URL à scraper
url = "https://www.jumia.sn/ordinateurs-accessoires-informatique/"  # Remplace par l'URL de ton choix

# ===============[FONCTIONS GENERIQUES]===============

def recuperer_page(url) :
    # Envoyer une requête GET
    try : 
        response = requests.get(url)
        if response.status_code // 200 == 1:
            # Analyser le HTML de la page
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        # Vérifier que la requête s'est bien passée
        else : return
    except Exception as e:
        print(e) 

def imprimer_json(chemin, donnees) : 
    with open(chemin, 'a', encoding='utf-8') as f:
        f.write(json.dumps(donnees, ensure_ascii=False, indent=4))


