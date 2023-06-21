# pip install streamlit, pandas, plotly, openpyxl 터미널 실행 후 작업 시작 

import pandas as pd
import streamlit as st
import plotly.express as px

# 제목 설정
st.set_page_config(page_title='투자운용사별 ETF 현황')
st.header('투자운용사별 ETF 현황')
st.subheader('상장종목수 & 순자산가치총액 & 일평균거래대금')

# 데이터 불러오기
excel_file = st.file_uploader(".xlsx 파일을 선택해주세요", type=['xlsx'])
if excel_file is not None:
    # Excel 파일을 DataFrame으로 읽어오기
    df = pd.read_excel(excel_file, sheet_name='Sheet1', usecols='A:F')

    # 그래프 설정
    colors = ['lightsteelblue', 'thistle', 'bisque']
    chart_titles = ['상장종목수', '순자산가치총액', '일평균거래대금']
    value_columns = ['상장종목수', '순자산가치총액', '일평균거래대금']

    # 그래프 그리기
    for title, value_column in zip(chart_titles, value_columns):
        fig = px.pie(df, values=value_column, names='구분', title=title, color_discrete_sequence=colors, hole=0.3)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)