from tkinter import Button
from click import option
import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
from datetime import datetime

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
     latest_iteration.text(f'iteration {i + 1}')
     bar.progress(i + 1)
     time.sleep(0.1)

'Done!!!!'

#condition = st.slider('あなたの今の調子は？', 0, 100, 50)
#'あなたの調子は', condition

#values = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0))
#st.write('Values:', values)

#from datetime import time
#appointment = st.slider(
#     "Schedule your appointment:",
#     value=(time(11, 30), time(12, 45)))
#st.write("You're scheduled for:", appointment)

#start_time = st.slider(
#     "When do you start?",
#     value=datetime(2020, 1, 1, 9, 30),
#     format="MM/DD/YY - hh:mm")
#st.write("Start time:", start_time)

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
     right_column.write('ここ右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
text = st.text
#left_column, right_column = st.beta_columns(2)
#left_column.button_input('あなたの趣味は？')
#condition = st.slider('あなたの調子は？',0,100,50)

#'あなたの趣味：', text
#'コンディション：', condition

#option = st.selectbox(
##    '誕生月は何月ですか。',
#    list(range(1,13))
#)
#option, '月はあなたの誕生月です。'

#if st.checkbox('Show Image'):
#    img = Image.open('c:\py\src\ironman.jpg')
#    st.image(img, caption='ironman', use_column_width=True)


