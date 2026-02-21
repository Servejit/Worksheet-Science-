import streamlit as st
import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Class 8 Science Exam", layout="centered")

DATA_FILE = "class8_students.json"

# ---------- Load Data ----------

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    students = json.load(f)


# ---------- Questions ONLY ----------

questions_only = [

"Ovaries, Testes, Hormones, Thyroid",

"Copper, Plastic, Aluminium, Iron",

"Myopia, Hypermetropia, Astigmatism, Retina",

"Focus, Epicentre, Fault, Richter",

"Adrenaline, Insulin, Thyroxine, Blood",

"Reflection, Refraction, Diffusion, Dispersion",

"Earthquake, Flood, Tsunami, Pollution",

"Menarche, Menopause, Adolescence, Childhood",

"Pituitary, Thyroid, Pancreas, Neuron",

"Retina, Cornea, Lens, Skin",

"Lightning, Earthquake, Cyclone, Growth",

"Positive charge, Negative charge, Neutral, Current",

"Vitamin A, Vitamin C, Vitamin D, Oxygen",

"Adolescence, Puberty, Childhood, Atom",

"Copper, Wood, Iron, Aluminium"

]


# ---------- Hidden Answer Key ----------

def get_answers():

    return [

"Hormones",

"Plastic",

"Retina",

"Richter",

"Blood",

"Diffusion",

"Pollution",

"Childhood",

"Neuron",

"Skin",

"Growth",

"Current",

"Oxygen",

"Atom",

"Wood"

]


# ---------- Certificate ----------

def create_certificate(name, score):

    filename = f"{name}_Certificate.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>CERTIFICATE OF ACHIEVEMENT</b>", styles["Title"]))

    story.append(Spacer(1,20))

    story.append(Paragraph(f"Awarded to <b>{name}</b>", styles["Normal"]))

    story.append(Spacer(1,20))

    story.append(Paragraph(f"Score: <b>{score}/15</b>", styles["Normal"]))

    doc.build(story)

    return filename



# ---------- UI ----------

st.title("SCIENCE WORKSHEET 2026")

name = st.text_input("Student Name")

if name in students:

    st.error("Already Attempted")

    st.stop()


# ---------- Questions ----------

student_answers = []

for i,q in enumerate(questions_only):

    st.write(f"{i+1}. {q}")

    ans = st.text_input("Odd One Out:", key=i)

    st.text_input("Reason:", key=f"r{i}")

    student_answers.append(ans)



# ---------- Submit ----------

if st.button("Submit"):

    answers = get_answers()

    score = 0

    for i in range(15):

        if student_answers[i].strip().lower() == answers[i].lower():

            score += 1

    students[name] = score

    with open(DATA_FILE,"w") as f:

        json.dump(students,f)

    st.success(f"Score: {score}/15")

    file = create_certificate(name, score)

    with open(file,"rb") as f:

        st.download_button("Download Certificate", f)



# ---------- Teacher Dashboard ----------

st.sidebar.title("Teacher Dashboard")

if st.sidebar.checkbox("Show Results"):

    for s in students:

        st.sidebar.write(s, students[s])
