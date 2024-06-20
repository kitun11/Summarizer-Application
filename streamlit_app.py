import google.generativeai as genai
import streamlit as st

import os
import pandas as pd
from sentence_transformers import SentenceTransformer

#configuring with the api key
os.environ['GOOGLE_API_KEY']="AIzaSyCzhGGTIEGuqvR-AjvmpqyGUnl7bXqofrs"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

#setting up model
model=genai.GenerativeModel('gemini-pro')

#setting up summaries as session states
if 'summary1' not in st.session_state:
    st.session_state.summary1="""
The 1983 Cricket World Cup, hosted by England, was a watershed moment in cricket history. India, captained by Kapil Dev, emerged as the surprise champions, defeating the dominant West Indies in the final.

Kapil Dev led from the front with his inspiring leadership and all-around contributions. The highest run-scorer of the tournament was David Gower of England, amassing 384 runs with his elegant batting. Meanwhile, the highest wicket-taker was Roger Binny of India, who claimed 18 wickets with his disciplined bowling.

India's victory in 1983 was not only a triumph for the team but also a pivotal moment for cricket in the country and beyond. It sparked a revolution, inspiring a generation of players and fans. Kapil Dev's leadership, along with standout performances from players like Gower and Binny, cemented the 1983 World Cup as one of the most memorable events in cricketing history, reshaping the sport's landscape and paving the way for India's future dominance in international cricket.
"""


if 'summary2' not in st.session_state:
    st.session_state.summary2="""
The 1987 Cricket World Cup, jointly hosted by India and Pakistan, featured several innovations in format and presentation, including colored clothing and floodlit matches. Australia emerged victorious under the captaincy of Allan Border, marking their first-ever World Cup triumph.

The highest run-scorer of the tournament was Graham Gooch of England, who showcased his batting prowess with a total of 471 runs. Meanwhile, the highest wicket-taker was Craig McDermott of Australia, who displayed his bowling excellence by claiming 18 wickets.

Australia's victory in 1987 marked a significant moment in cricketing history, as they demonstrated their all-around strength and resilience throughout the tournament. Allan Border's leadership, along with standout performances from players like Gooch and McDermott, propelled Australia to glory, leaving a lasting impact on the sport and paving the way for their future success in international cricket.
"""

if 'summary3' not in st.session_state:
    st.session_state.summary3="""
The 1992 Cricket World Cup, hosted by Australia and New Zealand, introduced several innovations to the game, including colored clothing and floodlit matches. Pakistan, captained by the legendary Imran Khan, emerged as the champions in a memorable tournament.

The highest run-scorer of the 1992 World Cup was Martin Crowe of New Zealand, who showcased his batting brilliance with a total of 456 runs. Meanwhile, Wasim Akram, also from Pakistan, stood out as the highest wicket-taker, claiming a total of 18 wickets with his exceptional bowling skills.

Imran Khan's leadership played a pivotal role in Pakistan's success, guiding the team through challenging moments to clinch the title. Crowe's batting prowess and Akram's bowling brilliance were crucial in shaping the tournament's outcome, cementing their places in cricketing history.

The 1992 World Cup not only showcased Pakistan's triumph but also left a lasting legacy with its innovative changes to the game. Imran Khan's captaincy, coupled with standout performances from Crowe and Akram, made the tournament a memorable chapter in cricket history.
"""

if 'summary4' not in st.session_state:
    st.session_state.summary4="""
The 1996 Cricket World Cup, co-hosted by India, Pakistan, and Sri Lanka, featured 12 teams and witnessed Sri Lanka emerge as champions for the first time, under the leadership of Arjuna Ranatunga.

The highest run-scorer of the tournament was Sachin Tendulkar of India, who showcased his batting brilliance with a total of 523 runs. Meanwhile, Anil Kumble, also from India, stood out as the highest wicket-taker, claiming a total of 15 wickets with his exceptional bowling skills.

Arjuna Ranatunga's captaincy played a pivotal role in Sri Lanka's historic victory, guiding the team with strategic brilliance and composure. Tendulkar's batting masterclass and Kumble's bowling prowess were instrumental in shaping the tournament's outcome, leaving an indelible mark on cricketing history.

The 1996 World Cup not only marked Sri Lanka's breakthrough triumph but also showcased the rising dominance of Asian cricket on the global stage. Ranatunga's leadership, coupled with standout performances from Tendulkar and Kumble, made the tournament a memorable chapter in cricket history, inspiring generations of cricketers in the subcontinent and beyond.
"""

if 'summary5' not in st.session_state:
    st.session_state.summary5="""
The 1999 Cricket World Cup, primarily hosted by England with matches in Ireland, Scotland, Wales, and the Netherlands, saw Australia emerge as champions for the second time, under the captaincy of Steve Waugh.

The highest run-scorer of the tournament was Rahul Dravid of India, who demonstrated his batting prowess with a total of 461 runs. Meanwhile, Geoff Allott of New Zealand stood out as the highest wicket-taker, claiming a total of 20 wickets with his exceptional bowling skills.

Steve Waugh's leadership was instrumental in Australia's successful campaign, guiding the team with tactical acumen and determination. Dravid's consistent batting performances and Allott's impactful bowling were crucial in shaping the tournament's outcome, contributing to Australia's triumph.

The 1999 World Cup not only reaffirmed Australia's cricketing supremacy but also showcased the competitive spirit and talent of players from around the world. Waugh's captaincy, coupled with standout performances from Dravid and Allott, made the tournament a memorable chapter in cricket history, solidifying Australia's status as a cricketing powerhouse.
"""

#display the summaries in the app
st.title("SEMANTIC SEARCH APPLICATION")
st.header("**1983 ODI Cricket World Cup Summary**")
st.write(st.session_state.summary1)
st.header("**1987 ODI Cricket World Cup Summary**")
st.write(st.session_state.summary2)
st.header("**1992 ODI Cricket World Cup Summary**")
st.write(st.session_state.summary3)
st.header("**1996 ODI Cricket World Cup Summary**")
st.write(st.session_state.summary4)
st.header("**1999 ODI Cricket World Cup Summary**")
st.write(st.session_state.summary5)

if 'pr' not in st.session_state:
    st.session_state.pr=False
if 'df' not in st.session_state:
    st.session_state.df=pd.DataFrame()
#generating dataframe
def dataframe_generator():
    li2 = []
    #global df
    def keypoints_extractor(summary):
        response6 = model.generate_content(
            f"Extract the year of World Cup, the country which won, the winning Captain, the highest run getter and the highest wicket taker from the following summary and return the answers in order, separated by a comma: {summary}")
        list1 = response6.text
        li = list(list1.split(", "))
        li2.append(li)
    keypoints_extractor(st.session_state.summary1)
    keypoints_extractor(st.session_state.summary2)
    keypoints_extractor(st.session_state.summary3)
    keypoints_extractor(st.session_state.summary4)
    keypoints_extractor(st.session_state.summary5)

    st.session_state.df = pd.DataFrame(li2, columns=['Year', 'Team', 'Captain', 'Highest Run Getter', 'Highest Wicket Taker'])
    st.session_state.pr=True





#following function converts any dataframe row into a corpus, calculates the similarity score with the particular summary in question and finally outputs the row with highest score.
def CreateCorpusFromDataFrame(summary,dataframe):

    model2 = SentenceTransformer("multi-qa-mpnet-base-cos-v1")
    similarities = []
    query_embedding = model2.encode(summary)
    for index, r in dataframe.iterrows():
        entry=""
        for col in dataframe.columns:
            text=r[col]
            entry+=" "+str(text)


        passage_embedding = model2.encode(entry)
        similarity = model2.similarity(query_embedding, passage_embedding)
        sim=similarity.item()
        similarities.append(sim)
        #print(f"{entry}\n")
        #print(f"Similarity: {sim}\n")
    x = similarities[0]
    y = 0
    for i in range(len(st.session_state['df'].iloc[[y]].axes[1])):
        if similarities[i] > x:
            x = similarities[i]
            y = i
    output=f"\nThe record of row {y+1}, i.e., row index {y} has the highest similarity score of {x}."

    st.write(output)
    st.write("**Relevant Record:**")
    st.write(dataframe.iloc[[y]])


#designing the app
st.button("Generate Dataframe",on_click=dataframe_generator)


if st.session_state.pr==True:
  
    st.write(st.session_state.df)
    st.write("**Select Summary:**")
    option = st.radio(
    label="Select the summary for which you want the semantic search to occur:",
    options=("Summary 1", "Summary 2", "Summary 3", "Summary 4", "Summary 5"),
    index=None
)
    if option == "Summary 1":

        CreateCorpusFromDataFrame(st.session_state.summary1, st.session_state.df)

    elif option == "Summary 2":

        CreateCorpusFromDataFrame(st.session_state.summary2, st.session_state.df)

    elif option == "Summary 3":

        CreateCorpusFromDataFrame(st.session_state.summary3, st.session_state.df)

    elif option == "Summary 4":

        CreateCorpusFromDataFrame(st.session_state.summary4, st.session_state.df)

    elif option == "Summary 5":

        CreateCorpusFromDataFrame(st.session_state.summary5, st.session_state.df)

    
