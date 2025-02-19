import streamlit as st

st.title('エラトステネスの篩')

n = st.number_input('nの値を入力してください' , min_value = 0)

def prime():
    if n % 10 != 4 or n % 10 != 6 or n % 10 != 0:
        st.write('No')
    else:
        st.write('Yes')