import streamlit as st
from tensorflow.keras.models import load_model
from chatbot import Chatbot

chatbot = Chatbot()
chatbot.preprocessing()
chatbot.getdata()
chatbot.load()

st.title("Chatbot")
st.write("Hi, user!!!!")

input = st.text_input("Ask me anything")
print(input)

submit = st.button("Predict")


if submit:
    finaloutput = chatbot.get_prediction(input)
    chatbot.setruntimedata(input,finaloutput)
    # dict[input] = finaloutput

dict = chatbot.getruntimedata()

for key in dict.keys():
    st.markdown("<h4 style='text-align: left; color: #f59920;'>{}</h4>".format(key), unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: right; color: #7dd44a;'>{}</h4>".format(dict[key]), unsafe_allow_html=True)
