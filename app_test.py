import streamlit as st

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt


# 메인 타이틀을 중앙에 달기

_, col, _ = st.columns([2,6,2])
col.header('Stream 시각화!!')

# 시각화 대상의 데이터
dfIris = sns.load_dataset('iris')
dfIris

colors = {"setosa":"red", "versicolor":"blue","virginica":"green"} 

with st.sidebar:
    selectX = st.selectbox("X 변수 선택 :", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    selectY = st.selectbox("Y 변수 선택 :", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    selectSpecies = st.multiselect("붓꽃 유형 선택 (다중) : ",["setosa","versicolor","virginica"])
    ''
    selectAlpha = st.slider("alpha 설정:", 0.1, 1.0, 0.5)

# 선택된 붓꽃 유형별 산점도로 시각화 표현
if selectSpecies:
    fig = plt.figure(figsize=(7,5))
    for aSpecies in selectSpecies:
        df = dfIris[dfIris.species == aSpecies]
        plt.scatter(df[selectX], df[selectY],color=colors[aSpecies],alpha= selectAlpha,label=aSpecies)
    
    plt.xlabel(selectX)
    plt.ylabel(selectY)
    plt.title("Iris Scatter Plot")
    st.pyplot(fig)
else:
    st.warning("붓꽃의 유형을 선택하세요")
