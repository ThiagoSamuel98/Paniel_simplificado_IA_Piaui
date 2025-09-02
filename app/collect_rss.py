import requests
import xml.etree.ElementTree as ET
import pandas as pd
from .utils import clean_text, save_to_csv

SEARCH_TERMS = ["Inteligência Artificial Piauí", "IA Piauí", "SIA Piauí"]

def collect_news():
    """Coleta no máximo 15 notícias do Google News RSS para os termos definidos."""
    all_items = []
    for term in SEARCH_TERMS:
        url = f"https://news.google.com/rss/search?q={term}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erro ao coletar notícias para: {term}")
            continue

        root = ET.fromstring(response.content)
        for item in root.findall(".//item"):
            if len(all_items) >= 15:   # Para quando já tiver 15
                break
            title = item.find("title").text if item.find("title") is not None else ""
            link = item.find("link").text if item.find("link") is not None else ""
            description = item.find("description").text if item.find("description") is not None else ""
            all_items.append({
                "title": clean_text(title),
                "description": clean_text(description),
                "link": link
            })

        if len(all_items) >= 15:  # Se já tiver 15, para de buscar em outros termos
            break

    df = pd.DataFrame(all_items)
    if not df.empty:
        save_to_csv(df, "data/news_raw.csv")
    return df

if __name__ == "__main__":
    df = collect_news()
    print(df.head())

