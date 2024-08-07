import fitz  # PyMuPDF
import pandas as pd
import requests

def download_and_process_pdf(url, output_csv="output.csv"):
    # PDFをダウンロード
    response = requests.get(url)
    with open("document.pdf", "wb") as f:
        f.write(response.content)

    # PDFを開く
    document = fitz.open("document.pdf")

    # データを保持するリスト
    data = []

    # PDFの各ページを読み込む
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text("text")

        # テキストを行ごとに分割
        lines = text.split("\n")

        # 各行を処理
        for line in lines:
            # ここで行の内容を処理してデータを抽出
            data.append(line.split())  # スペースで区切る場合

    # DataFrameに変換
    df = pd.DataFrame(data)

    # CSVとして保存
    df.to_csv(output_csv, index=False, header=False)
    print(f"CSVファイルが作成されました：{output_csv}")

    return df
