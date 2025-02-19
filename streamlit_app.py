import streamlit as st

st.title('エラトステネスの篩')

n = st.number_input('nの値を入力してください' , min_value = 0)

origin = []

for i in range(10 ** 60):
    if i != 1:
        origin.append(i)

j = 2

while j > 10 ** 60 / 2:
    if j == origin[0]:
        for k in origin:
            if origin[k] % j == 0:
                origin.pop(k)

st.write(origin)

def prime():
    if n % 10 != 4 or n % 10 != 6 or n % 10 != 0:
        st.write('No')
    else:
        pass