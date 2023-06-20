import streamlit as st
import plotly.graph_objects as go
import random
import pandas as pd

# 데이터생성
df = pd.read_csv("C:\\Users\\Ham\\OneDrive\\바탕 화면\\데이터분석스쿨\\krx_data_2022_trade.csv")

# 차트 그리기
fig = go.Figure(data=[go.Pie(df)])
fig.update_layout(
    title="[파이차트]",              # 제목 추가
    title_x = 0.5,                  # 제목 가운데 정렬
    legend_traceorder="normal",     # 범례 정렬
)

# 차트 출력
st.plotly_chart(fig)
