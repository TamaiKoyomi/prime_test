import streamlit as st

st.title('ぱう')

#n = st.number_input('nの値を入力してください' , min_value = 0)

for i in range(10 ** 5):
    a = i ** 2 + 1
    st.write(str(i) + ':' + str(a))