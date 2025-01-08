import streamlit as st
import random

st.title("나의 첫번째 앱")
st.text('\n\n')
st.write('안녕하세요. 저는 🤣🎗️입니다')
st.write('저의 이메일 주소, jinyusang063@gmail.com')

st.button("리셋", type="primary")
if st.button("난수 생성"):
    st.write(random.randint(1,1000))
else:
    st.write("卍解")
