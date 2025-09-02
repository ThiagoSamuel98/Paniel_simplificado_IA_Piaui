import re
import pandas as pd

def clean_text(text: str) -> str:
    """Remove HTML tags, caracteres especiais e normaliza espaços."""
    text = re.sub(r"<.*?>", "", text)  # Remove tags HTML
    text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)  # Remove caracteres especiais
    text = re.sub(r"\s+", " ", text)  # Remove espaços extras
    return text.strip()

def save_to_csv(data: pd.DataFrame, path: str):
    """Salva DataFrame em CSV."""
    data.to_csv(path, index=False, encoding="utf-8")
