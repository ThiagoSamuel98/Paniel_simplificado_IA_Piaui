import pandas as pd
from .utils import save_to_csv

def load_keywords(path: str) -> list:
    """Carrega lista de palavras-chave de um arquivo de texto."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

def classify_sentiment(text: str, positive_words, negative_words) -> str:
    """Classifica o sentimento baseado em regras simples."""
    text_lower = text.lower()
    pos_count = sum(word in text_lower for word in positive_words)
    neg_count = sum(word in text_lower for word in negative_words)

    if pos_count > neg_count:
        return "positivo"
    elif neg_count > pos_count:
        return "negativo"
    else:
        return "neutro"

def process_news(input_csv="data/news_raw.csv", output_csv="data/news_processed.csv"):
    """Processa notícias: classifica sentimentos e salva CSV final."""
    df = pd.read_csv(input_csv)

    positive_words = load_keywords("app/keywords/positive_ptbr.txt")
    negative_words = load_keywords("app/keywords/negative_ptbr.txt")

    df["sentiment"] = df["description"].apply(
        lambda x: classify_sentiment(str(x), positive_words, negative_words)
    )

    save_to_csv(df, output_csv)
    return df

if __name__ == "__main__":
    df = process_news()
    print(df.head())
