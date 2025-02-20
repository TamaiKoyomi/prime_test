import streamlit as st
import math

st.title('ぱう')

n = st.number_input('nの値を入力してください' , min_value = 0)

po = n * n + 1

def is_prime_optimized(n):
    if n <= 1:
        return False
    if n <= 3:  # 2と3は素数
        return True
    if n % 2 == 0 or n % 3 == 0:  # 2と3の倍数は素数でない
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if st.button('計算'):
    st.write(is_prime_optimized(po))