import streamlit as st 
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


@st.cache_data # used to save entire data into the cache so that will not load each and everyrime from that particular library 
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df['species'] = iris.target
    return df , iris.target_names

df,target_names = load_data()

model = RandomForestClassifier()
# to train a model
model.fit(df.iloc[:,:-1],df['species']) # df.iloc[:,:-1] - independent feature , ,df['species'] - dependent feature

st.sidebar.title("Input Feature")
sepal_length = st.sidebar.slider("Sepal length", float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal width", float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal length", float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal width", float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))


input_data =[[sepal_length,sepal_width,petal_length,petal_width]]


#prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]


st.write("Prediction")
st.write("The predicted species is :",{predicted_species})
