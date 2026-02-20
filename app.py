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

# ---------- 25 MCQs ----------

questions = [

("Female loses reproductive ability at 45–50:", ["Menarche","Menstruation","Menopause","Peripause"], "Menopause"),

("Endocrine chemical messengers:", ["Hormones","Sperms","Eggs","None"], "Hormones"),

("Atom loses electron becomes:", ["Negative","Positive","Neutral","None"], "Positive"),

("Good conductor has many:", ["Bound","Free","Floating","Flying"], "Free"),

("Blurring distant vision:", ["Hypermetropia","Myopia","Astigmatism","Night blindness"], "Myopia"),

("Reflection from rough surface:", ["Regular","Multiple","Diffused","None"], "Diffused"),

("Earthquake origin point:", ["Epicentre","Focus","Fault","None"], "Focus"),

("Lightning rod material:", ["Bakelite","Plastic","Wood","Copper"], "Copper"),

("Puberty to adulthood period:", ["Adolescence","Childhood","Adult","None"], "Adolescence"),

("Like charges:", ["Attract","Repel","Both","None"], "Repel"),

("Image formed on:", ["Cornea","Retina","Lens","None"], "Retina"),

("Earthquake scale:", ["Richter","Barometer","Meter","None"], "Richter"),

("First menstrual flow:", ["Menarche","Menopause","Ovulation","None"], "Menarche"),

("Normal cycle:", ["7","10","20","28"], "28"),

("Oestrogen produced by:", ["Testes","Pituitary","Pancreas","Ovaries"], "Ovaries"),

("Not natural calamity:", ["Earthquake","Flood","Tsunami","Deforestation"], "Deforestation"),

("Magnitude measured by:", ["Barometer","Manometer","Richter","None"], "Richter"),

("Point above focus:", ["Plate","Fault","Focus","Epicentre"], "Epicentre"),

("Master gland:", ["Pituitary","Thyroid","Pancreas","None"], "Pituitary"),

("Growth hormone gland:", ["Thyroid","Pituitary","Adrenal","None"], "Pituitary"),

("Fight flight hormone:", ["Adrenaline","Insulin","Thyroxine","None"], "Adrenaline"),

("Secondary sexual characteristics:", ["Hormones","Cells","Bones","None"], "Hormones"),

("Electrolysis is:", ["Chemical reaction","Physical change","Both","None"], "Chemical reaction"),

("Night blindness cause:", ["Vitamin A deficiency","Vitamin C","Vitamin D","None"], "Vitamin A deficiency"),

("Lightning safety:", ["Stay indoors","Stand tree","Use lift","None"], "Stay indoors"),

]

# ---------- Writing Questions ----------

writing_questions = [

"What is adolescence?",

"Define electrolysis.",

"What is myopia?",

"What is tsunami?",

"Explain endocrine system."

]

# ---------- Certificate ----------

def create_certificate(name, score):

    filename = f"{name}_Class8_Certificate.pdf"

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

    story.append(Paragraph("<font size=18>Class VIII Science Annual Exam 2026</font>", styles["Normal"]))

    doc.build(story)

    return filename

# ---------- UI ----------

st.title("SAMPLE WORKSHEET 2026")
st.header("Class VIII Science")

name = st.text_input("Student Name")
class_name = st.text_input("Class")

if name in students:

    st.error("You already attempted exam")

    st.stop()

# ---------- MCQs ----------

answers = []

for i,q in enumerate(questions):

    st.write(f"{i+1}. {q[0]}")

    ans = st.radio("", q[1], key=i)

    answers.append(ans)

# ---------- Writing ----------

st.header("Writing Section")

for w in writing_questions:

    st.text_area(w, height=120)

# ---------- Submit ----------

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

    file = create_certificate(name, score)

    with open(file,"rb") as f:

        st.download_button("Download Certificate", f, file_name=file)

# ---------- Teacher Dashboard ----------

st.sidebar.title("Teacher Dashboard")

if st.sidebar.checkbox("Show Results"):

    for s in students:

        st.sidebar.write(f"{s} : {students[s]}/25")
