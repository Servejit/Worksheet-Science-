import streamlit as st
import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Class 7 Science Exam", layout="centered")

DATA_FILE = "class7_students.json"

# ---------------- LOAD DATA ----------------

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    students = json.load(f)

# ---------------- 25 MCQs ----------------

questions = [

("Strawberries propagate through:", ["Grafting","Tissue culture","Layering","Stolon"], "Stolon"),

("Flowers with only stamens:", ["Bisexual","Unisexual","Homosexual","None"], "Unisexual"),

("SI unit of speed:", ["km/h","km/s","m/h","m/s"], "m/s"),

("Crawling baby motion:", ["Uniform","Circular","Non-uniform","Periodic"], "Non-uniform"),

("Automatic electric safety device:", ["Fuse","MCB","Relay","Maglev"], "MCB"),

("Potential difference unit:", ["Joule","Newton","Volt","Watt"], "Volt"),

("Concave lens forms:", ["Real","Virtual","Both","None"], "Virtual"),

("Solar cooker uses mirror:", ["Plane","Convex","Concave","Any"], "Concave"),

("Opposition to current:", ["Voltage","Resistance","Speed","Power"], "Resistance"),

("Diverging lens:", ["Convex","Concave","Plane","None"], "Concave"),

("Same flower pollination:", ["Cross","Self","Artificial","None"], "Self"),

("Electric start stop device:", ["Switch","Volt","Ampere","None"], "Switch"),

("Plane mirror image:", ["Virtual erect","Real erect","Virtual inverted","Real inverted"], "Virtual erect"),

("Mirror showing lateral inversion:", ["Plane","Convex","Concave","All"], "All"),

("Real image formed by:", ["Concave mirror","Plane mirror","Convex mirror","None"], "Concave mirror"),

("Female gamete part:", ["Ovary","Style","Ovule","Sepal"], "Ovule"),

("Pollen tube grows in:", ["Ovary","Style","Anther","Sepal"], "Style"),

("Pollen found in:", ["Stigma","Anther","Ovary","Style"], "Anther"),

("Transfer pollen called:", ["Fertilisation","Germination","Pollination","Reproduction"], "Pollination"),

("Pollen received by:", ["Ovary","Anther","Stigma","Sepal"], "Stigma"),

("Fuse used for:", ["Safety","Light","Heat","None"], "Safety"),

("Electromagnet used in:", ["Crane","Fan","Bulb","Switch"], "Crane"),

("Rear view mirror:", ["Convex","Concave","Plane","None"], "Convex"),

("Speed formula:", ["Distance/time","Time/distance","Distance×time","None"], "Distance/time"),

("Reproduction modes:", ["2","3","4","5"], "2"),

]

# ---------------- WRITING QUESTIONS ----------------

writing_questions = [

"What is reproduction? Name its types.",

"Define speed and formula.",

"What is electric circuit?",

"Explain pollination types.",

"Explain reflection of light."

]

# ---------------- CERTIFICATE ----------------

def create_certificate(name, score):

    filename = f"{name}_Class7_Certificate.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<font size=34 color=darkblue><b>🏆 CERTIFICATE OF ACHIEVEMENT 🏆</b></font>", styles["Title"]))

    story.append(Spacer(1,30))

    story.append(Paragraph("<font size=22>This certificate is proudly awarded to</font>", styles["Normal"]))

    story.append(Spacer(1,20))

    story.append(Paragraph(f"<font size=30 color=green><b>{name}</b></font>", styles["Title"]))

    story.append(Spacer(1,20))

    story.append(Paragraph(f"<font size=22>For scoring <b>{score}/25</b></font>", styles["Normal"]))

    story.append(Spacer(1,20))

    story.append(Paragraph("<font size=24 color=red>🌟 Excellent Performance 🌟</font>", styles["Title"]))

    story.append(Spacer(1,20))

    story.append(Paragraph("<font size=18>Class VII Science Annual Exam 2026</font>", styles["Normal"]))

    doc.build(story)

    return filename

# ---------------- UI ----------------

st.title("SAMPLE WORKSHEET 2026")
st.header("Class VII Science")

name = st.text_input("Student Name")
class_name = st.text_input("Class")

if name in students:

    st.error("You already attempted exam")

    st.stop()

# ---------------- QUESTIONS ----------------

answers = []

for i,q in enumerate(questions):

    st.write(f"{i+1}. {q[0]}")

    ans = st.radio("", q[1], key=i)

    answers.append(ans)

# ---------------- WRITING ----------------

st.header("Writing Section")

for w in writing_questions:

    st.text_area(w, height=120)

# ---------------- SUBMIT ----------------

if st.button("Submit Exam"):

    score = 0

    for i,q in enumerate(questions):

        if answers[i] == q[2]:

            score += 1

    students[name] = score

    with open(DATA_FILE,"w") as f:

        json.dump(students,f)

    st.balloons()

    st.markdown(f"# 🎉 SCORE: {score} / 25 🎉")

    st.markdown("## 🎁 Congratulations 🎁")

    file = create_certificate(name, score)

    with open(file,"rb") as f:

        st.download_button("Download Certificate", f, file_name=file)

# ---------------- TEACHER DASHBOARD ----------------

st.sidebar.title("Teacher Dashboard")

if st.sidebar.checkbox("Show Results"):

    for s in students:

        st.sidebar.write(f"{s} : {students[s]}/25")
