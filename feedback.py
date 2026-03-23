import streamlit as st
import pandas as pd

st.title("🎬 Видео правки для DaVinci Resolve")

# Клиент вставляет ссылку
video_url = st.text_input("📎 Ссылка на видео (Mega/ЯДиск):")

if video_url:
    # Автоопределение сервиса + iframe
    if 'mega.nz' in video_url:
        # Mega плеер
        st.components.v1.iframe(video_url, height=450)
    elif 'disk.yandex.ru' in video_url:
        # ЯДиск превью
        st.components.v1.iframe(video_url, height=450)
    else:
        # Обычный плеер
        st.video(video_url)
    
    if 'markers' not in st.session_state:
        st.session_state.markers = []
    
    st.subheader("Маркеры")
    current_time = st.slider("⏱️ Время (сек):", 0, 7200, 0)
    note = st.text_input("💬 Правка:")
    
    col1, col2 = st.columns([3,1])
    with col2:
        if st.button("📍 Маркер") and note:
            timecode = f"{current_time//3600:02d}:{(current_time%3600)//60:02d}:{current_time%60:02d}"
            st.session_state.markers.append({"Timecode": timecode, "Note": note})
            st.success(f"✅ {timecode}")
            st.rerun()
    
    if st.session_state.markers:
        df = pd.DataFrame(st.session_state.markers)
        st.dataframe(df)
        csv = df.to_csv(index=False)
        st.download_button("💾 CSV для Resolve", csv, "markers.csv")
else:
    st.info("👆 Вставьте ссылку с Mega.nz или Яндекс.Диска")
