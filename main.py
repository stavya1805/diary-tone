import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import glob

filepaths = sorted (glob.glob("diary/*.txt"))
print(filepaths)


positivity = []
negativity = []
analyzer = SentimentIntensityAnalyzer()

for filepath in filepaths:
    with open (filepath,"r") as file:
        content = file.read()
    moods_dict = analyzer.polarity_scores(content)
    positivity.append(moods_dict['pos'])
    negativity.append(moods_dict['neg'])

dates = [filepath.strip(".txt").strip("diary\\") for filepath in filepaths]
print(dates)

st.title("Diary Tone")

st.header("Positivity")
figure = px.line(x=dates,y=positivity,labels={"x":"Dates","y":"Positivity"})
st.plotly_chart(figure)

st.header("Negativity")
figure = px.line(x=dates,y=negativity,labels={"x":"Dates","y":"Negativity"})
st.plotly_chart(figure)


