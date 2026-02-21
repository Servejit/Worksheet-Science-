import streamlit as st
import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Class 7 Science Worksheet", layout="centered")

DATA_FILE = "class7_students.json"

# ---------------- LOAD DATA ----------------

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    students = json.load(f)


# ---------------- QUESTIONS ----------------

questions_only = [

"Stolon, Grafting, Tissue culture, Speed",

"Stamen, Ovule, Style, Fuse",

"m/s, Volt, Ampere, Distance",

"Uniform motion, Circular motion, Non-uniform motion, Pollination",

"Fuse, MCB, Switch, Ovary",

"Volt, Resistance, Speed, Style",

"Concave lens, Convex lens, Plane mirror, Ovule",

"Plane mirror, Concave mirror, Convex mirror, Pollination",

"Resistance, Voltage, Current, Ovary",

"Convex mirror, Concave mirror, Plane mirror, Speed",

"Self pollination, Cross pollination, Fertilisation, Fuse",

"Switch, MCB, Fuse, Ovule",

"Virtual image, Real image, Resistance, Inverted image",

"Concave mirror, Convex mirror, Plane mirror, Ovule",

"Pollination, Fertilisation, Germination, Fuse"

]


# ---------------- HIDDEN ANSWERS ----------------

def get_answers():

    return [

"Speed",

"Fuse",

"Distance",

"Pollination",

"Ovary",

"Style",

"Ovule",

"Pollination",

"Ovary",

"Speed",

"Fuse",

"Ovule",

"Resistance",

"Ovule",

"Fuse"

]


# ---------------- CERTIFICATE ----------------

def create_certificate(name, score):

    filename = f"{name}_Class7_Certificate.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<font size=34><b>CERTIFICATE OF ACHIEVEMENT</b></font>", styles["Title"]))

    story.append(Spacer(1,30))

    story.append(Paragraph(f"<font size=24>This is awarded to <b>{name}</b></font>", styles["Normal"]))

    story.append(Spacer(1,20))

    story.append(Paragraph(f"<font size=22>Score: {score}/15</font>", styles["Normal"]))

    story.append(Spacer(1,20))

    story.append(Paragraph("<font size=18>Class VII Science Worksheet 2026</font>", styles["Normal"]))

    doc.build(story)

    return filename


# ---------------- UI ----------------

st.title("SCIENCE WORKSHEET 2026")
st.header("Class VII")

name = st.text_input("Student Name")
class_name = st.text_input("Class")

if name in students:

    st.error("You already attempted exam")

    st.stop()


# ---------------- QUESTIONS DISPLAY ----------------

student_answers = []

st.header("Odd One Out")

for i,q in enumerate(questions_only):

    st.write(f"{i+1}. {q}")

    ans = st.text_input("Odd One Out:", key=i)

    st.text_input("Reason:", key=f"reason{i}")

    student_answers.append(ans)

    st.write("")


# ---------------- SUBMIT ----------------

if st.button("Submit Exam"):

    correct_answers = get_answers()

    score = 0

    wrong_list = []

    for i in range(len(correct_answers)):

        student = student_answers[i].strip()
        correct = correct_answers[i]

        if student.lower() == correct.lower():

            score += 1

        else:

            wrong_list.append((questions_only[i], student, correct))


    students[name] = score

    with open(DATA_FILE,"w") as f:

        json.dump(students,f)


    st.balloons()

    st.markdown(f"# 🎉 SCORE: {score} / 15 🎉")


    # -------- REVIEW SECTION --------

    if wrong_list:

        st.error("Review Your Mistakes")

        for item in wrong_list:

            st.write(f"Question: {item[0]}")

            st.write(f"❌ Your Answer: {item[1]}")

            st.write(f"✅ Correct Answer: {item[2]}")

            st.write("---")

    else:

        st.success("Perfect Score! All Correct")


    # -------- CERTIFICATE --------

    file = create_certificate(name, score)

    with open(file,"rb") as f:

        st.download_button("Download Certificate", f, file_name=file)



# ---------------- TEACHER DASHBOARD ----------------

st.sidebar.title("Teacher Dashboard")

if st.sidebar.checkbox("Show Results"):

    for s in students:

        st.sidebar.write(f"{s} : {students[s]}/15")
