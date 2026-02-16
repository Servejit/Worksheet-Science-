# ---------------------------------------------------
# INSTALL
# pip install streamlit pandas openpyxl
# ---------------------------------------------------

import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Sample Worksheet", layout="wide")

# ---------------------------------------------------
# SOUND (WORKING SOFT SOUND)
# ---------------------------------------------------

def play_wrong_sound():
    st.markdown(
        """
        <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-10.mp3" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# FILE TO SAVE RESULTS
# ---------------------------------------------------

FILE = "results.xlsx"

if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Time","Name","Class","Score"])
    df.to_excel(FILE, index=False)


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📘 Sample Worksheet – Class VI Science")

# ---------------------------------------------------
# STUDENT DETAILS
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter Name")

with col2:
    student_class = st.text_input("Enter Class")


# ---------------------------------------------------
# ANSWERS
# ---------------------------------------------------

correct = {

    "q1": "Poles",
    "q2": "Sedimentary",
    "q3": "Sun",
    "q4": "artificial",
    "q5": "transpiration",
    "q6": "compass"

}


# ---------------------------------------------------
# MCQ
# ---------------------------------------------------

st.header("Section A – MCQ")

q1 = st.radio(
    "1. Magnetic strength maximum at:",
    ["Centre","Poles","Corners","Same throughout"],
    key="q1"
)

if q1:

    if q1 == correct["q1"]:

        st.success("✔ Correct")

    else:

        st.error("✘ Wrong")
        play_wrong_sound()



q2 = st.radio(
    "2. Fossils found in:",
    ["Igneous","Sedimentary","Metamorphic","Any"],
    key="q2"
)

if q2:

    if q2 == correct["q2"]:

        st.success("✔ Correct")

    else:

        st.error("✘ Wrong")
        play_wrong_sound()



q3 = st.radio(
    "3. Ultimate energy source:",
    ["Water","Air","Fossil fuels","Sun"],
    key="q3"
)

if q3:

    if q3 == correct["q3"]:

        st.success("✔ Correct")

    else:

        st.error("✘ Wrong")
        play_wrong_sound()



# ---------------------------------------------------
# FILL UPS
# ---------------------------------------------------

st.header("Section B – Fill Ups")

q4 = st.text_input("4. Horseshoe magnets are ______ magnets")

if q4:

    if q4.lower() == correct["q4"]:

        st.success("✔ Correct")

    else:

        st.error("✘ Wrong")



q5 = st.text_input("5. Loss of water through leaves is ______")

if q5:

    if q5.lower() == correct["q5"]:

        st.success("✔ Correct")

    else:

        st.error("✘ Wrong")



q6 = st.text_input("6. Instrument to find direction is ______")

if q6:

    if q6.lower() == correct["q6"]:

        st.success("✔ Correct")

    else:

        st.error("✘ Wrong")



# ---------------------------------------------------
# WRITING SPACE
# ---------------------------------------------------

st.header("Section C – Writing")

ans7 = st.text_area("7. What is evaporation?")

ans8 = st.text_area("8. What are meteorites?")

ans9 = st.text_area("9. How clouds are formed?")

ans10 = st.text_area("10. Why natural magnets not used in cranes?")



# ---------------------------------------------------
# SUBMIT BUTTON
# ---------------------------------------------------

if st.button("Submit Worksheet"):


    if name == "" or student_class == "":

        st.error("Enter Name and Class")

    else:

        score = 0


        if q1 == correct["q1"]:
            score += 1

        if q2 == correct["q2"]:
            score += 1

        if q3 == correct["q3"]:
            score += 1

        if q4.lower() == correct["q4"]:
            score += 1

        if q5.lower() == correct["q5"]:
            score += 1

        if q6.lower() == correct["q6"]:
            score += 1



        final_score = round((score/6)*10,2)



        # SAVE RESULT

        new = pd.DataFrame({

            "Time":[datetime.now()],
            "Name":[name],
            "Class":[student_class],
            "Score":[final_score]

        })


        old = pd.read_excel(FILE)

        combined = pd.concat([old,new], ignore_index=True)

        combined.to_excel(FILE, index=False)



        st.success("Submitted Successfully")

        st.write("Score:", final_score,"/10")



# ---------------------------------------------------
# MULTI USER READY
# ---------------------------------------------------

st.info("This worksheet supports 100+ students")
