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

FILE = "results.xlsx"

# ---------------------------------------------------
# CREATE FILE
# ---------------------------------------------------

if not os.path.exists(FILE):

    pd.DataFrame(columns=["Name","Class","Score","Time"]).to_excel(FILE,index=False)


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

data = pd.read_excel(FILE)


# ---------------------------------------------------
# CERTIFICATE FUNCTION
# ---------------------------------------------------

def create_certificate(name, student_class, score):

    file_name = f"certificate_{name}.pdf"

    c = canvas.Canvas(file_name, pagesize=A4)

    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(300,750,"Certificate of Achievement")

    c.setFont("Helvetica",18)

    c.drawCentredString(300,650,f"This is to certify that")

    c.setFont("Helvetica-Bold",22)
    c.drawCentredString(300,600,name)

    c.setFont("Helvetica",18)
    c.drawCentredString(300,550,f"Class: {student_class}")

    c.drawCentredString(300,500,f"Score: {score} / 10")

    c.drawCentredString(300,400,"Excellent Performance 🎉")

    c.save()

    return file_name


# ---------------------------------------------------
# TEACHER DASHBOARD
# ---------------------------------------------------

mode = st.sidebar.selectbox(

"Select Mode",

["Student","Teacher Dashboard"]

)

# ---------------------------------------------------
# TEACHER MODE
# ---------------------------------------------------

if mode=="Teacher Dashboard":

    st.title("📊 Teacher Dashboard")

    st.dataframe(data,use_container_width=True)

    st.download_button(

    "Download Results Excel",

    open(FILE,"rb"),

    file_name="Results.xlsx"

    )

    st.stop()


# ---------------------------------------------------
# STUDENT MODE
# ---------------------------------------------------

st.title("📘 Science Worksheet")

name = st.text_input("Enter Name")

student_class = st.text_input("Enter Class")


# ---------------------------------------------------
# CHECK ATTEMPT
# ---------------------------------------------------

if name in data["Name"].values:

    st.error("❌ You already attempted")

    st.stop()


# ---------------------------------------------------
# QUESTIONS
# ---------------------------------------------------

correct={

"q1":"Poles",
"q2":"Sedimentary",
"q3":"Sun",
"q4":"artificial",
"q5":"transpiration",
"q6":"compass"

}

score=0


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
# SUBMIT
# ---------------------------------------------------

if st.button("Submit"):


    if name=="" or student_class=="":

        st.error("Enter details")

    else:


        score=0

        if q1==correct["q1"]: score+=1
        if q2==correct["q2"]: score+=1
        if q3==correct["q3"]: score+=1
        if q4.lower()==correct["q4"]: score+=1
        if q5.lower()==correct["q5"]: score+=1
        if q6.lower()==correct["q6"]: score+=1


        final=round(score/6*10,2)


        # SAVE

        new=pd.DataFrame({

        "Name":[name],
        "Class":[student_class],
        "Score":[final],
        "Time":[datetime.now()]

        })

        pd.concat([data,new]).to_excel(FILE,index=False)


        # RESULT DISPLAY

        st.balloons()

        st.markdown(

        f"<h1 style='text-align:center;color:green;font-size:80px;'>🎯 {final}/10</h1>",

        unsafe_allow_html=True

        )


        # GIFTS

        if final==10:

            st.success("🏆 Gift: Gold Trophy")

        elif final>=8:

            st.success("⭐ Gift: Star Medal")

        elif final>=6:

            st.success("🍫 Gift: Chocolate")

        else:

            st.success("😊 Gift: Keep Practicing")


        # CERTIFICATE

        cert=create_certificate(name,student_class,final)

        with open(cert,"rb") as f:

            st.download_button(

            "🏆 Download Certificate",

            f,

            file_name=cert

            )
