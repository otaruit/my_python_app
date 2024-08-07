import streamlit as st
import pandas as pd
import chardet

from scraping import download_and_process_pdf

# 使用するPDFのURL
pdf_url = "https://www.city.otaru.lg.jp/docs/2020111000476/file_contents/20240730.pdf"

# 関数を呼び出して処理を行う
df = download_and_process_pdf(pdf_url)


# アップロードされたファイルをデータフレームに読み込む
if df is not None:
    
    # 検出されたエンコーディングでファイルを読み込む
    # df = pd.read_csv(df)
    
    # データフレームを表示
    st.write(df)
