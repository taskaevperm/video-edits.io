import streamlit as st
import pandas as pd

st.title("🎬 Видео правки")
video_url = "https://disk.yandex.ru/i/sgAy4Bg3uRmVSg"
st.video(video_url)

if 'markers' not in st.session_state:
    st.session_state.markers = []

current_time = st.slider("Перейти к моменту (сек):", 0, 3600, 0)
note = st.text_input("Правка:")

if st.button("📍 Поставить маркер") and note:
    seconds = current_time
    timecode = f"{seconds//3600:02d}:{(seconds%3600)//60:02d}:{seconds%60:02d}"
    st.session_state.markers.append({"Timecode": timecode, "Note": note})
    st.success(f"Маркер: {timecode} - {note}")
    st.rerun()

if st.session_state.markers:
    st.subheader("Маркеры")
    df = pd.DataFrame(st.session_state.markers)
    st.dataframe(df)
    csv = df.to_csv(index=False)
    st.download_button("📥 Скачать CSV для Resolve", csv, "markers.csv", "text/csv")
