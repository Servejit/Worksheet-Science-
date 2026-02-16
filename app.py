import streamlit as st
import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- CONFIG ----------------

st.set_page_config(page_title="Class 6 Science Test", layout="centered")

DATA_FILE = "students.json"

# ---------------- LOAD DATA ----------------

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    students = json.load(f)

# ---------------- QUESTIONS ----------------

questions = [

("Nickel is:", ["Magnetic", "Non Magnetic", "Liquid", "Gas"], "Magnetic"),

("Magnetic strength is maximum at:", ["Centre", "Pole", "Side", "None"], "Pole"),

("Rate of evaporation decreases when:", ["Area increases", "Area decreases", "Heat increases", "Wind increases"], "Area decreases"),

("Water conservation done by:", ["Recycling", "Planting trees", "Stopping pollution", "All"], "All"),

("Ultimate energy source:", ["Water", "Sun", "Coal", "Air"], "Sun"),

("Fossils found in:", ["Igneous", "Sedimentary", "Metamorphic", "None"], "Sedimentary"),

("Brightest planet:", ["Earth", "Venus", "Mars", "Mercury"], "Venus"),

("Universe studied by:", ["Astronomer", "Doctor", "Engineer", "Pilot"], "Astronomer"),

("Compass used for:", ["Direction", "Speed", "Distance", "Weight"], "Direction"),

("Coal formed from:", ["Plants", "Animals", "Water", "Air"], "Plants"),

("Magnet has poles:", ["1", "2", "3", "4"], "2"),

("Like poles:", ["Attract", "Repel", "Neutral", "None"], "Repel"),

("Unlike poles:", ["Repel", "Attract", "Neutral", "None"], "Attract"),

("Water vapour change to water:", ["Condensation", "Evaporation", "Melting", "Freezing"], "Condensation"),

("Water vapour rises due to:", ["Heat", "Cold", "Pressure", "None"], "Heat"),

("Earth suitable due to:", ["Air", "Water", "Temperature", "All"], "All"),

("Meteorites fall on:", ["Earth", "Moon", "Sun", "Mars"], "Earth"),

("Artificial magnets used in:", ["Cranes", "Fans", "Lights", "Cars"], "Cranes"),

("Transpiration is:", ["Water loss", "Water gain", "Heat loss", "Heat gain"], "Water loss"),

("Water cycle includes:", ["Evaporation", "Condensation", "Rain", "All"], "All"),

("Natural magnet:", ["Magnetite", "Iron", "Nickel", "Cobalt"], "Magnetite"),

("Magnetic substance:", ["Iron", "Plastic", "Wood", "Paper"], "Iron"),

("Planet gives light:", ["Sun", "Venus", "Mars", "None"], "None"),

("Cloud formed by:", ["Condensation", "Evaporation", "Freezing", "Melting"], "Condensation"),

("Energy from sun called:", ["Solar", "Wind", "Water", "Coal"], "Solar"),

]

# ---------------- WRITING QUESTIONS ----------------

writing_questions = [

"Explain water cycle",

"What is magnet?",

"Define evaporation",

"Why earth suitable for life?",

"Explain solar energy importance"

]

# ---------------- CERTIFICATE ----------------

def create_certificate(name, score):

    filename = f"{name}_certificate.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<font size=32 color=blue><b>CERTIFICATE OF ACHIEVEMENT</b></font>", styles["Title"]))

    story.append(Spacer(1,20))

    story.append(Paragraph("<font size=20>This certificate is proudly presented to</font>", styles["Normal"]))

    story.append(Spacer(1,10))

    story.append(Paragraph(f"<font size=28 color=green><b>{name}</b></font>", styles["Title"]))

    story.append(Spacer(1,10))

    story.append(Paragraph(f"<font size=20>For scoring <b>{score}/25</b> in Science Test</font>", styles["Normal"]))

    story.append(Spacer(1,30))

    story.append(Paragraph("<font size=24 color=red>🏆 Excellent Performance 🏆</font>", styles["Title"]))

    doc.build(story)

    return filename

# ---------------- TITLE ----------------

st.title("ANNUAL EXAMINATION 2026")
st.header("Class 6 Science Test")

name = st.text_input("Student Name")
class_name = st.text_input("Class")

# ---------------- ONE ATTEMPT ----------------

if name in students:

    st.error("You have already attempted the test")

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

if st.button("Submit Test"):

    score = 0

    for i,q in enumerate(questions):

        if answers[i] == q[2]:

            score += 1

    students[name] = score

    with open(DATA_FILE,"w") as f:

        json.dump(students,f)

    st.balloons()

    st.markdown(f"# 🎉 Your Score: {score} / 25 🎉")

    st.markdown("## 🎁 Congratulations 🎁")

    file = create_certificate(name, score)

    with open(file,"rb") as f:

        st.download_button("Download Certificate", f, file_name=file)

# ---------------- TEACHER DASHBOARD ----------------

st.sidebar.title("Teacher Dashboard")

if st.sidebar.checkbox("Show Results"):

    for s in students:

        st.sidebar.write(f"{s} : {students[s]}/25")
