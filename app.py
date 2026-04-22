import streamlit as st
import random
import time
from streamlit_paste_button import paste_image_button  # 追加

st.set_page_config(page_title="Hyper AI Checker", page_icon="🤖")

st.title("🤖 次世代AI パル/ポケ判定システム")
st.write("最新の技術と独自の画像認識アルゴリズムを用いて、アップロードされた画像を瞬時に解析・分類します。")

# --- 画像入力エリア（ファイル選択 or コピペボタン） ---
st.write("画像をアップロードするか、クリップボードから直接貼り付けてください。")

col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("フォルダから選ぶ", type=["jpg", "png"], label_visibility="collapsed")
with col2:
    st.write("または")
    paste_result = paste_image_button(
        label="📋 コピーした画像を貼り付け",
        background_color="#FF4B4B",
        hover_background_color="#FF0000"
    )

# どちらかから画像が入力されたら、変数 img_data に格納する
img_data = None
if uploaded_file is not None:
    img_data = uploaded_file
elif paste_result.image_data is not None:
    img_data = paste_result.image_data

# --- 解析処理 ---
if img_data is not None:
    st.image(img_data, caption='解析ターゲット', use_container_width=True)
    
    with st.status("AIコアが画像を解析中...", expanded=True) as status:
        st.write("🔍 画像から特徴量を抽出しています...")
        time.sleep(1)
        st.write("🧠 巨大ニューラルネットワークに照会中...")
        time.sleep(1.5)
        st.write("⚡ 最終判定アルゴリズムを実行中...")
        time.sleep(1)
        status.update(label="解析プロセス完了", state="complete", expanded=False)
    
    results = [
        "【判定: ポケモン】\n確信度: 99.8% (最新のアルゴリズムがそう言っています)",
        "【判定: パルワールド】\n確信度: 98.5% (最新のアルゴリズムがそう言っています)",
        "【判定: エラー】\n画像が複雑すぎます。おそらく実写の猫か何かです。",
        "【判定: デジモン】\n確信度: 120% (最新のアルゴリズムがそう言っています)"
    ]
    ans = random.choice(results)
    
    st.success("解析が完了しました。以下の結果をご確認ください。")
    st.subheader(ans)
    
    st.write("---")
    st.caption("※本システムは最先端の「乱数（Randomモジュール）」を利用して高度な判定を行っています。いかなる公式企業・団体とも一切関係ありません。")
