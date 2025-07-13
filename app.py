import streamlit as st

st.title('Title!')

a = st.radio('select ' , ['a' , 'b' , 'c'] , index  = None)

b = st.slider('Select the length : ' , min_value = 6 , max_value = 32 , value = 8)

upper = st.toggle('d')
digits = st.toggle('e')
sign = st.toggle('f')

st.write('HI!!!!!!!!!!!1')

st.selectbox('Seperator : ' , ['-' , '_' , ',' , '.'])

