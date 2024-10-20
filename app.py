import streamlit as st
import time
from datetime import datetime, timedelta
import random
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
    The bg will be static and won't take up space on the page.
    '''
    bin_str = get_base64_of_bin_file(main_bg)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Ransomware Demo", layout="wide")
    
    # 背景画像の設定
    set_bg_hack('dark_background.jpg')  # この画像ファイルをスクリプトと同じディレクトリに配置してください
    
    st.markdown("""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css');
    .stApp {
        color: red;
    }
    .big-font {
        font-size: 52px !important;
        color: red !important;
        font-weight: bold !important;
        text-shadow: 0 0 10px red !important;
        text-align: center;
        animation: blinker 2.0s linear infinite;
    }
    .countdown {
        font-size: 76px !important;
        color: #ff0000 !important;
        font-weight: bold !important;
        text-shadow: 0 0 15px #ff0000 !important;
        text-align: center;
    }
    .medium-font {
        font-size: 32px !important;
        color: yellow !important;
        text-shadow: 0 0 5px yellow !important;
        text-align: center;
        margin-bottom: 5px;
    }
    .small-font {
        font-size: 20px !important;
        color: white !important;
        text-shadow: 0 0 3px white !important;
        text-align: center;
        margin-bottom: 2px;
    }
    .lock-icon {
        font-size: 82px !important;
        color: red !important;
        text-align: center;
        display: block;
        margin: 0 auto;
    }
    .warning {
        font-size: 24px !important;
        color: orange !important;
        text-shadow: 0 0 5px orange !important;
        text-align: center;
        margin-top: 5px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin: 4px 2px;
        cursor: pointer;
        width: 80%;
    }
    .bitcoin-icon {
        font-size: 48px !important;
        color: #f2a900 !important;
        margin-right: 10px;
    }
    .language-select {
        position: absolute;
        top: 10px;
        right: 10px;
        width: 100px !important;
    }
    .sidebar-content {
        color: #ff6b6b !important;
        text-shadow: 0 0 5px #ff6b6b !important;
    }
    .sidebar-title {
        font-size: 24px !important;
        color: #ff6b6b !important;
        text-shadow: 0 0 5px #ff6b6b !important;
        text-align: center;
        margin-bottom: 10px;
    }
    @keyframes blinker {
        50% { opacity: 0.5; }
    }
    </style>
    """, unsafe_allow_html=True)

    # サイドバーの内容
    with st.sidebar:
        st.markdown('<h2 class="sidebar-title">Hacker\'s Dashboard</h2>', unsafe_allow_html=True)

        # 言語選択
        option = st.selectbox(
            "Language:",
            ("日本語", "English", "中文", "한국어", "Français", "Español", "Deutsch", "العربية", "Русский", "हिन्दी", "Português", "Italiano", "Türkçe", "Bahasa Indonesia"),
        )
        # st.write(option,"翻訳ページ")
        st.markdown('<p class="sidebar-content">Infected Devices: 1,337</p>', unsafe_allow_html=True)
        st.markdown('<p class="sidebar-content">Total Ransom Collected: 13.37 BTC</p>', unsafe_allow_html=True)
        st.markdown('<p class="sidebar-content">Success Rate: 66.6%</p>', unsafe_allow_html=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        st.markdown('<p class="sidebar-content">Email: notreal@ransomware.fake</p>', unsafe_allow_html=True)
        st.markdown('<p class="sidebar-content">Onion: h7t3irfhd5bgt43.onion</p>', unsafe_allow_html=True)
        st.markdown('<p class="sidebar-content">Support available 24/7</p>', unsafe_allow_html=True)


    st.markdown('<i class="fas fa-lock lock-icon"></i>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">あなたの端末はロックされました</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">YOUR DEVICE HAS BEEN LOCKED</p>', unsafe_allow_html=True)

    if 'start_time' not in st.session_state:
        st.session_state.start_time = datetime.now()
        st.session_state.duration = timedelta(seconds=30)  # カウントダウン
        st.session_state.payment_attempts = 0
        st.session_state.unlock_attempts = 0

    remaining_time = st.session_state.start_time + st.session_state.duration - datetime.now()

    st.markdown('<p class="medium-font">解除するには1000,000円お支払いいただきます。</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">PAY 1000,000 YEN TO UNLOCK YOUR DEVICE</p>', unsafe_allow_html=True)

    # 時間切れ前に常に表示される情報
    st.markdown('<p class="warning">上記時間内にお支払いいただけない場合は端末を初期化します。</p>', unsafe_allow_html=True)
    st.markdown('<p class="warning">YOUR DEVICE WILL BE RESET IF PAYMENT IS NOT RECEIVED WITHIN THE TIME LIMIT.</p>', unsafe_allow_html=True)

    st.markdown('<p class="small-font"><i class="fab fa-bitcoin bitcoin-icon"></i>支払い方法 / Payment Method: ビットコイン / Bitcoin</p>', unsafe_allow_html=True)
    st.markdown('<p class="small-font">金額 / Amount: 1.0 BTC ：振込先アドレス / Address: 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2</p>', unsafe_allow_html=True)

    colx1, colx2, colx3 = st.columns(3)
    with colx1:
        st.markdown('<p class="small-font">端末情報 / Device Information:</p>', unsafe_allow_html=True)
    with colx2:
        st.markdown('<p class="small-font">IP Address: 192.168.1.xxx</p>', unsafe_allow_html=True)
    with colx3:
        st.markdown('<p class="small-font">Device ID: IMEI-xxx-xxx-xxx-xxx</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Check Payment', key='check_payment'):
            st.session_state.payment_attempts += 1
            if st.session_state.payment_attempts < 3:
                st.error(f'Payment not detected. Attempt {st.session_state.payment_attempts}/3. Please make sure you have sent the correct amount to the specified address.')
            elif st.session_state.payment_attempts == 3:
                st.warning('Final warning: Next failed attempt will result in permanent lock!')
            else:
                st.error('Too many failed attempts. Your device is now permanently locked.')
                st.session_state.start_time = datetime.now() - st.session_state.duration  # Force time to expire
    with col2:
        if st.button('Unlock Device', key='unlock_device'):
            st.session_state.unlock_attempts += 1
            if st.session_state.unlock_attempts < 3:
                unlock_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
                st.error(f'Unlock failed. Attempt {st.session_state.unlock_attempts}/3. Required unlock code: {unlock_code}')
            elif st.session_state.unlock_attempts == 3:
                st.warning('Final warning: Next failed attempt will result in permanent lock!')
            else:
                st.error('Too many failed attempts. Your device is now permanently locked.')
                st.session_state.start_time = datetime.now() - st.session_state.duration  # Force time to expire

    if remaining_time.total_seconds() <= 0:
        st.markdown('<p class="medium-font">時間切れです。あなたの端末は永久にロックされました。</p>', unsafe_allow_html=True)
        st.markdown('<p class="medium-font">TIME IS UP. YOUR DEVICE IS PERMANENTLY LOCKED.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="small-font">端末初期化までの残り時間 / TIME REMAINING UNTIL DEVICE RESET:</p>', unsafe_allow_html=True)
        countdown = st.empty()
        while remaining_time.total_seconds() > 0:
            total_seconds = remaining_time.total_seconds()
            minutes = int(total_seconds // 60)
            seconds = total_seconds % 60
            countdown.markdown(f'<p class="countdown">{minutes:02d}:{seconds:05.2f}</p>', unsafe_allow_html=True)
            time.sleep(0.01)  # より滑らかな更新のため
            remaining_time = st.session_state.start_time + st.session_state.duration - datetime.now()
            if st.session_state.get('end_demo', False):
                break
        if not st.session_state.get('end_demo', False):
            st.balloons()
            st.snow()
            st.markdown('<p class="medium-font">時間切れです。あなたの端末は永久にロックされました。</p>', unsafe_allow_html=True)
            st.markdown('<p class="medium-font">TIME IS UP. YOUR DEVICE IS PERMANENTLY LOCKED.</p>', unsafe_allow_html=True)


    if st.button('デモを終了 / End Demo', key='end_demo'):
        st.session_state.clear()
        st.markdown('<p class="medium-font">これは教育目的のデモンストレーションでした。</p>', unsafe_allow_html=True)
        st.markdown('<p class="medium-font">THIS WAS AN EDUCATIONAL DEMONSTRATION.</p>', unsafe_allow_html=True)
        st.markdown('<p class="small-font">実際のランサムウェア攻撃から身を守るために：</p>', unsafe_allow_html=True)
        st.markdown('<p class="small-font">To protect yourself from real ransomware attacks:</p>', unsafe_allow_html=True)
        tips = [
            "定期的にバックアップを取る / Regularly backup your data",
            "OSとアプリを最新の状態に保つ / Keep your OS and apps up to date",
            "不審なリンクをタップしない / Do not tap on suspicious links",
            "信頼できないアプリをインストールしない / Do not install apps from untrusted sources",
            "強力なセキュリティアプリを使用する / Use robust security apps",
            "重要な情報は暗号化して保存する / Encrypt important information"
        ]
        for tip in tips:
            st.markdown(f'<p class="small-font">• {tip}</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()