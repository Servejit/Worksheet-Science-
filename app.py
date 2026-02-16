import streamlit as st
import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ---------------- CONFIG ----------------

st.set_page_config(page_title="Class 6 Science Worksheet", layout="centered")

DATA_FILE = "students.json"

# ---------------- LOAD DATA ----------------

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    students = json.load(f)

# ---------------- SOUNDS ----------------

wrong_sound = """
<audio autoplay>
<source src="https://www.soundjay.com/buttons/sounds/button-10.mp3" type="audio/mp3">
</audio>
"""

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

    story.append(Paragraph("<font size=30 color=blue><b>CERTIFICATE OF ACHIEVEMENT</b></font>", styles["Title"]))

    story.append(Spacer(1,20))

    story.append(Paragraph(f"<font size=20>This is to certify that</font>", styles["Normal"]))

    story.append(Spacer(1,10))

    story.append(Paragraph(f"<font size=25 color=green><b>{name}</b></font>", styles["Title"]))

    story.append(Spacer(1,10))

    story.append(Paragraph(f"<font size=20>has scored {score}/25 in Science Test</font>", styles["Normal"]))

    story.append(Spacer(1,30))

    story.append(Paragraph("🎉 Excellent Work 🎉", styles["Title"]))

    doc.build(story)

    return filename

# ---------------- TITLE ----------------

st.title("Class 6 Science Test")

name = st.text_input("Student Name")
class_name = st.text_input("Class")

# ---------------- ONE ATTEMPT ----------------

if name in students:

    st.error("Already attempted")

    st.stop()

# ---------------- QUIZ ----------------

score = 0

answers = []

for i,q in enumerate(questions):

    st.write(f"{i+1}. {q[0]}")

    ans = st.radio("", q[1], key=i)

    answers.append(ans)

    if ans:

        if ans == q[2]:

            st.success("Correct")

        else:

            st.error("Wrong")

            st.markdown(wrong_sound, unsafe_allow_html=True)

# ---------------- WRITING ----------------

st.header("Writing Section")

for i,w in enumerate(writing_questions):

    st.text_area(w, height=100)

# ---------------- SUBMIT ----------------

if st.button("Submit"):

    for i,q in enumerate(questions):

        if answers[i] == q[2]:

            score += 1

    students[name] = score

    with open(DATA_FILE,"w") as f:

        json.dump(students,f)

    st.balloons()

    st.markdown(f"# 🎉 Your Score: {score}/25 🎉")

    st.markdown("## 🎁🎁 Congratulations 🎁🎁")

    file = create_certificate(name,score)

    with open(file,"rb") as f:

        st.download_button("Download Certificate", f, file_name=file)

# ---------------- TEACHER DASHBOARD ----------------

st.sidebar.title("Teacher Dashboard")

if st.sidebar.checkbox("Show"):

    for s in students:

        st.sidebar.write(s, students[s])
