import streamlit as st
import pandas as pd
import monty_hall   # a file in my repository

st.write('HI!!!!!!!!!!!')

"""
Author : Ehsan \n
Date : 25/13/7 \n 
Streamlit \n
"""

st.title('Title!')

a = st.radio('select ' , ['a' , 'b' , 'c'] , index  = None)

b = st.slider('Select the length : ' , min_value = 6 , max_value = 32 , value = 8)

upper = st.toggle('d')
digits = st.toggle('e')
sign = st.toggle('f')



st.selectbox('Seperator : ' , ['-' , '_' , ',' , '.'])

df = pd.DataFrame({
    'first column' : [1 , 2 , 3 , 4] , 
    'second column' : [11 , 22 , 33 , 44]
})

df

st.multiselect('select :' , ['alpha' , 'beta' , 'gamma' , 'teta'])


st.line_chart(df)

col1 , col2 , col3 = st.columns(3)

col1.write("I'm first!")

col2.write("I'm second!")

col3.write("I'm third!")

col1.checkbox('check 1')
col3.checkbox('check 3')
col2.checkbox('check 2')

col1.text_input('Write a text')
col2.text_input('Write a text' , placeholder = 'text')
col3.number_input('Write a number' , min_value = 0 , max_value = 1000 , placeholder = 17)
col3.number_input('Number' , value = None , placeholder = 7 , format = '%.0f')


range_game = st.number_input('Number of game count' , min_value = 1 , max_value = 100000r , placeholder = 10)
result = []
for i in range(range_game) :
    result.append(monty_hall.play(i + 1))
result = pd.DataFrame(result)

col11 , col22 = st.columns(2)
col11.subheader('win % with switch')
col22.subheader('win % without switch')

col11.line_chart(result[0])
col22.line_chart(result[1])
