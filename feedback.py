{\rtf1\ansi\ansicpg1251\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import re\
\
st.title("\uc0\u55356 \u57260  \u1042 \u1080 \u1076 \u1077 \u1086  \u1087 \u1088 \u1072 \u1074 \u1082 \u1080 ")\
video_url = "https://disk.yandex.ru/i/sgAy4Bg3uRmVSg"  # \uc0\u1042 \u1072 \u1096 \u1077  \u1074 \u1080 \u1076 \u1077 \u1086 \
st.video(video_url)\
\
# \uc0\u1052 \u1072 \u1088 \u1082 \u1077 \u1088 \u1099 \
if 'markers' not in st.session_state:\
    st.session_state.markers = []\
\
current_time = st.slider("\uc0\u1055 \u1077 \u1088 \u1077 \u1081 \u1090 \u1080 :", 0, 3600, 0) / 100  # \u1089 \u1077 \u1082 \u1091 \u1085 \u1076 \u1099 \
note = st.text_input("\uc0\u1055 \u1088 \u1072 \u1074 \u1082 \u1072 :")\
\
if st.button("\uc0\u55357 \u56525  \u1055 \u1086 \u1089 \u1090 \u1072 \u1074 \u1080 \u1090 \u1100  \u1084 \u1072 \u1088 \u1082 \u1077 \u1088 ") and note:\
    timecode = f"\{int(current_time//3600):02d\}:\{int((current_time%3600)//60):02d\}:\{int(current_time%60):02d\}"\
    st.session_state.markers.append(\{"Timecode": timecode, "Note": note\})\
    st.success(f"\uc0\u1052 \u1072 \u1088 \u1082 \u1077 \u1088 : \{timecode\} - \{note\}")\
\
# \uc0\u1058 \u1072 \u1073 \u1083 \u1080 \u1094 \u1072  \u1084 \u1072 \u1088 \u1082 \u1077 \u1088 \u1086 \u1074 \
if st.session_state.markers:\
    st.subheader("\uc0\u1052 \u1072 \u1088 \u1082 \u1077 \u1088 \u1099 ")\
    df = pd.DataFrame(st.session_state.markers)\
    st.dataframe(df)\
    st.download_button("\uc0\u55357 \u56549  \u1057 \u1082 \u1072 \u1095 \u1072 \u1090 \u1100  CSV \u1076 \u1083 \u1103  Resolve", df.to_csv(index=False), "markers.csv")\
}