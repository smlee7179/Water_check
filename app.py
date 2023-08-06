import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Thingspeak API URL과 API Key
thingspeak_url = "https://api.thingspeak.com/channels/2234450/feeds.json"
api_key = "68O6CHYLIJADYHIG"
st.set_option('deprecation.showPyplotGlobalUse', False)

# Thingspeak로부터 데이터 받아오기
def get_thingspeak_data(channel_id, api_key):
    url = f"{thingspeak_url}?api_key={api_key}&results=2"
    response = requests.get(url)
    data = response.json()
    feeds = data.get('feeds', [])
    df = pd.DataFrame(feeds)
    return df

# Streamlit 애플리케이션
def main():
    st.title("Thingspeak 물양 차트")

    # Thingspeak 데이터 받아오기
    df = get_thingspeak_data(channel_id="2234450", api_key=api_key)

    if df.empty:
        st.warning("데이터를 받아오지 못했습니다. Thingspeak 채널 ID와 API Key를 확인해주세요.")
        return

    # 데이터 확인
    st.subheader("물양 데이터")
    st.dataframe(df)

    # 시각화
    st.subheader("물양 차트")
    plt.figure(figsize=(10, 6))
    plt.plot(df['created_at'], df['field1'], marker='o')
    plt.xlabel("시간")
    plt.ylabel("물양")
    plt.xticks(rotation=45)
    st.pyplot()

if __name__ == "__main__":
    main()

