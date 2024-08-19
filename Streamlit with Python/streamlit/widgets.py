import streamlit as st 
import pandas as pd
st.title("Streamlit Text Input")
name = st.text_input("Enter your name : ")
if name:
    st.write("Hello",{name})
age = st.slider("Select your age",0,100,25)
st.write("Your age is ",{age})
options = {"python","java","c++","c"}
choice = st.selectbox("Choose your favorite programming ",options)
data = {
    "Name" : ["Insha","Sadaf","Ali","Neha"],
    "Age" :[25,22,29,19],
    "City" :["New York","India","Iraq","France"]
}
df = pd.DataFrame(data)
st.write(df)
df.to_csv("sample_data.csv")
uploaded_file = st.file_uploader("Choose a csv file",type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

