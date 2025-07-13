import streamlit as st
import pandas as pd


st.write('HI!!!!!!!!!!!')

"""
Author : Ehsan
Date : 25/13/7
Streamlit
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
