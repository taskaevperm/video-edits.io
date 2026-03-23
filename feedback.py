import streamlit as st
import pandas as pd

st.title("🎬 Видео правки для DaVinci Resolve")

# Поддержка Mega/Яндекс.Disk/VK через iframe
video_url = st.text_input("📎 Ссылка на видео (Mega/ЯДиск/VK):")

if video_url:
    # Iframe для облачных плееров
    st.components.v1.iframe(video_url, height=400)
    
    if 'markers' not in st.session_state:
        st.session_state.markers = []
    
    current_time = st.slider("⏱️ Перейти (сек):", 0, 7200, 0)
    note = st.text_input("💬 Правка:")
    
    if st.button("📍 Маркер") and note:
        seconds = current_time
        timecode = f"{seconds//3600:02d}:{(seconds%3600)//60:02d}:{seconds%60:02d}"
        st.session_state.markers.append({"Timecode": timecode, "Note": note})
        st.success(f"✅ {timecode} - {note}")
        st.rerun()
    
    if st.session_state.markers:
        st.subheader("📋 Маркеры")
        df = pd.DataFrame(st.session_state.markers)
        st.dataframe(df)
        csv = df.to_csv(index=False)
        st.download_button("💾 CSV для Resolve", csv, "markers.csv")
else:
    st.info("👆 Вставьте ссылку Mega/ЯДиск")
