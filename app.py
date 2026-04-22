import streamlit as st
import random
import time
from streamlit_paste_button import paste_image_button

# --- 画面の基本設定 ---
st.set_page_config(page_title="Hyper AI Checker", page_icon="🤖")

st.title("🤖 次世代AI パル/ポケモン判定システム")
st.write("最新の独自の画像認識アルゴリズムを用いて、画像を瞬時に解析・分類します。")

# --- 画像入力エリア ---
st.write("### 📸 画像を入力してください")
# PCならこのボタンを押す（またはフォーカスしてCtrl+V）だけで貼り付け可能
paste_result = paste_image_button(
    label="📋 クリップボードから画像を貼り付け",
    background_color="#FF4B4B",
    hover_background_color="#FF0000",
    errors="ignore"
)

# 従来のアップローダーも一応残しておきます（スマホ用など）
uploaded_file = st.file_uploader("または、ファイルをドラッグ＆ドロップ", type=["jpg", "png"], label_visibility="collapsed")

# どちらかに入力があった場合に処理を開始
img_data = None
if paste_result.image_data is not None:
    img_data = paste_result.image_data
elif uploaded_file is not None:
    img_data = uploaded_file

if img_data is not None:
    # 表示サイズを抑えめに設定 (width=300)
    st.image(img_data, caption='解析ターゲット', width=300)
    
    with st.status("AIコアが画像を解析中...", expanded=True) as status:
        st.write("🔍 特徴量を抽出中...")
        time.sleep(1.5)
        st.write("🧠 ニューラルネットワーク照会中...")
        time.sleep(2)
        st.write("⚡ 最終判定を実行中...")
        time.sleep(2)
        status.update(label="解析プロセス完了", state="complete", expanded=False)
    
    # --- 判定ロジック（確率調整） ---
    res_list = [
        "【判定: ポケモン】\n確信度: 99.8% (まあほぼ間違いないだろう、と最新のアルゴリズムが言っています)",
        "【判定: パルワールドのパル】\n確信度: 98.5% (これは完全にパル。最新のアルゴリズムがそう言っています)",
        "【判定: デジモン】\n確信度: 120% (騙そうったってそうはいかないと、最新のアルゴリズムが言っています)"
    ]
    
    # 重み付け: ポケ(3) + パル(3) + デジ(2) = 合計8。 2/8 = 25% (4回に1回)
    weights = [3, 3, 2]
    ans = random.choices(res_list, weights=weights)[0]
    
    st.success("解析が完了しました。")
    st.subheader(ans)
    
    st.write("---")
    st.caption("※本システムは最先端の「乱数（Randomモジュール）」を利用して高度な判定を行っています。いかなる公式企業・団体とも一切関係ありません。")
