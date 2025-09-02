import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def load_data(path="data/news_processed.csv"):
    return pd.read_csv(path)

def sentiment_pie_chart(df):
    fig, ax = plt.subplots()
    df["sentiment"].value_counts().plot.pie(autopct="%1.1f%%", ax=ax)
    ax.set_ylabel("")
    st.pyplot(fig)

def wordcloud_chart(df):
    text = " ".join(df["description"].dropna().astype(str))
    wc = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

def main():
    st.title("📊 Monitor IA no Piauí")
    st.markdown("Análise simplificada de notícias sobre **Inteligência Artificial no Piauí**")

    df = load_data()

    st.subheader("Distribuição de Sentimentos")
    sentiment_pie_chart(df)

    st.subheader("Nuvem de Palavras")
    wordcloud_chart(df)

    st.subheader("Notícias Coletadas")
    st.dataframe(df[["title", "sentiment", "link"]])

    st.markdown("---")
    st.caption("⚠️ Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.")

if __name__ == "__main__":
    main()
