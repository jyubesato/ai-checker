import streamlit as st
import random
import time

# --- 画面の基本設定 ---
st.set_page_config(page_title="Hyper AI Checker", page_icon="🤖")

st.title("🤖 次世代AI パル/ポケモン判定システム")
st.write("最新の独自の画像認識アルゴリズムを用いて、アップロードされた画像を瞬時に解析・分類します。")

# --- 画像入力エリア ---
uploaded_file = st.file_uploader("画像をドラッグ＆ドロップするか、枠内をクリックして Ctrl+V で貼り付け！", type=["jpg", "png"])

if uploaded_file is not None:
    # 表示サイズを抑えめに設定 (width=400)
    st.image(uploaded_file, caption='解析ターゲット', width=400)
    
    with st.status("AIコアが画像を解析中...", expanded=True) as status:
        st.write("🔍 特徴量を抽出中...")
        time.sleep(1.5)
        st.write("🧠 ニューラルネットワーク照会中...")
        time.sleep(2)
        st.write("⚡ 最終判定を実行中...")
        time.sleep(2)
        status.update(label="解析プロセス完了", state="complete", expanded=False)
    
    # --- 判定ロジック（確率調整） ---
    # 選択肢から「エラー」を削除
    res_list = [
        "【判定: ポケモン】\n確信度: 99.8% (まあほぼ間違いないだろう、と最新のアルゴリズムが言っています)",
        "【判定: パルワールドのパル】\n確信度: 98.5% (これは完全にパル。最新のアルゴリズムがそう言っています)",
        "【判定: デジモン】\n確信度: 120% (騙そうったってそうはいかないと、最新のアルゴリズムが言っています)"
    ]
    
    # 確率を重み付け (ポケ: 3, パル: 3, デジ: 2) 
    # 合計8のうち2回（＝25%）がデジモンになります
    weights = [3, 3, 2]
    ans = random.choices(res_list, weights=weights)[0]
    
    st.success("解析が完了しました。")
    st.subheader(ans)
    
    st.write("---")
    st.caption("※本システムは最先端の「乱数（Randomモジュール）」を利用して高度な判定を行っています。いかなる公式企業・団体とも一切関係ありません。")
