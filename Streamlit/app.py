# import streamlit as st


# st.title("Python For Data Science")

# st.header("Hello World! I am learning Python for Data Science")


# st.image('download (1).png')


# st.button('Predict')


# st.radio('Gender', ['Male', 'Female'])

# st.selectbox('Pick your option', ['Nigga Noob', 'Nigga Pro', 'Nigga Max'])


# st.multiselect('Pick your option', ['Nigga 1', 'Nigga 2', 'Nigga 3', 'Nigga 4'])


import streamlit as st
import numpy as np

from predict import  predict_diabetes


st.title('Diabetes Predictor App')

st.image('download (1).png')

st.write('Input your data and check your diabetes:')


glucose = st.number_input("Enter Glucose level:", 0, 400,100)

dp = st.number_input("Enter DP:", 0,10,7)

age = st.number_input("Enter Age:", 0,70,30)



if(st.button('Predict')):
    input_data = [[glucose, dp, age]]

    prediction = predict_diabetes(input_data)

    print(prediction)

    if prediction[0]==0:
        st.success("No diabetes.")
        st.balloons()
    else:
        st.warning("Sugar Kaam Khaya Kar Bhai")
