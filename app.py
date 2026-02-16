# ---------------------------------------------------
# INSTALL
# pip install streamlit pandas openpyxl reportlab
# ---------------------------------------------------

import streamlit as st
import pandas as pd
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

st.set_page_config(page_title="Science Worksheet", layout="wide")

FILE="results.xlsx"

# ---------------------------------------------------
# CREATE FILE
# ---------------------------------------------------

if not os.path.exists(FILE):

    pd.DataFrame(columns=[

    "Name","Class","Score","Time",

    "Evaporation","Meteorites",

    "Clouds","Magnets"

    ]).to_excel(FILE,index=False)


data=pd.read_excel(FILE)


# ---------------------------------------------------
# CERTIFICATE
# ---------------------------------------------------

def create_certificate(name,student_class,score):

    file=f"certificate_{name}.pdf"

    c=canvas.Canvas(file,pagesize=A4)

    c.setFont("Helvetica-Bold",30)

    c.drawCentredString(300,750,"Certificate")

    c.setFont("Helvetica",20)

    c.drawCentredString(300,650,name)

    c.drawCentredString(300,600,f"Class: {student_class}")

    c.drawCentredString(300,550,f"Score: {score}/10")

    c.save()

    return file


# ---------------------------------------------------
# MODE
# ---------------------------------------------------

mode=st.sidebar.selectbox(

"Mode",

["Student","Teacher Dashboard"]

)

# ---------------------------------------------------
# TEACHER
# ---------------------------------------------------

if mode=="Teacher Dashboard":

    st.title("Teacher Dashboard")

    st.dataframe(data,use_container_width=True)

    st.download_button(

    "Download Excel",

    open(FILE,"rb"),

    file_name="results.xlsx"

    )

    st.stop()


# ---------------------------------------------------
# STUDENT
# ---------------------------------------------------

st.title("Science Worksheet")

name=st.text_input("Name")

student_class=st.text_input("Class")


# ONE ATTEMPT

if name in data["Name"].values:

    st.error("You already attempted")

    st.stop()


# ---------------------------------------------------
# OBJECTIVE
# ---------------------------------------------------

correct={

"q1":"Poles",

"q2":"Sedimentary",

"q3":"Sun",

"q4":"artificial",

"q5":"transpiration",

"q6":"compass"

}


st.header("Objective")

q1=st.radio("Magnetic strength maximum at:",

["Centre","Poles","Corners","Same"])

q2=st.radio("Fossils found in:",

["Igneous","Sedimentary","Metamorphic","Any"])

q3=st.radio("Energy source:",

["Water","Air","Fossil fuels","Sun"])

q4=st.text_input("Horseshoe magnets are")

q5=st.text_input("Loss of water through leaves")

q6=st.text_input("Direction instrument")


# ---------------------------------------------------
# WRITING QUESTIONS
# ---------------------------------------------------

st.header("Writing Questions")

w1=st.text_area("What is evaporation?")

w2=st.text_area("What are meteorites?")

w3=st.text_area("How clouds are formed?")

w4=st.text_area("Why natural magnets not used in cranes?")


# ---------------------------------------------------
# SUBMIT
# ---------------------------------------------------

if st.button("Submit"):


    if name=="" or student_class=="":

        st.error("Enter details")

    else:


        score=0

        if q1==correct["q1"]:score+=1
        if q2==correct["q2"]:score+=1
        if q3==correct["q3"]:score+=1
        if q4.lower()==correct["q4"]:score+=1
        if q5.lower()==correct["q5"]:score+=1
        if q6.lower()==correct["q6"]:score+=1


        final=round(score/6*10,2)


        # SAVE

        new=pd.DataFrame({

        "Name":[name],

        "Class":[student_class],

        "Score":[final],

        "Time":[datetime.now()],

        "Evaporation":[w1],

        "Meteorites":[w2],

        "Clouds":[w3],

        "Magnets":[w4]

        })


        pd.concat([data,new]).to_excel(FILE,index=False)


        # RESULT

        st.balloons()

        st.markdown(

        f"<h1 style='text-align:center;color:green;font-size:80px;'>🎯 {final}/10</h1>",

        unsafe_allow_html=True

        )


        st.success("Saved")


        # CERTIFICATE

        cert=create_certificate(name,student_class,final)

        st.download_button(

        "Download Certificate",

        open(cert,"rb"),

        file_name=cert

        )
