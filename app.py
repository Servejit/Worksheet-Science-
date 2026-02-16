# ---------------------------------------------------
# INSTALL REQUIREMENTS:
# pip install streamlit reportlab
# ---------------------------------------------------

import streamlit as st
import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import base64
from datetime import datetime

st.set_page_config(page_title="Quiz App", layout="wide")

# ---------------- FILES ----------------

USER_FILE = "users.json"
RESULT_FILE = "results.json"

# create files if not exist
if not os.path.exists(USER_FILE):
    json.dump({}, open(USER_FILE, "w"))

if not os.path.exists(RESULT_FILE):
    json.dump({}, open(RESULT_FILE, "w"))


# ---------------- LOAD SAVE ----------------

def load_users():
    return json.load(open(USER_FILE))


def save_users(data):
    json.dump(data, open(USER_FILE, "w"))


def load_results():
    return json.load(open(RESULT_FILE))


def save_results(data):
    json.dump(data, open(RESULT_FILE, "w"))


# ---------------- QUESTIONS ----------------

questions = [

    {
        "type": "mcq",
        "question": "Capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },

    {
        "type": "mcq",
        "question": "2 + 2 = ?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },

    {
        "type": "write",
        "question": "Write 5 lines about yourself"
    },

    {
        "type": "write",
        "question": "Why do you want this gift?"
    }

]


# ---------------- SOUND ----------------

def play_sound():

    sound = """
    <audio autoplay>
    <source src="https://www.soundjay.com/buttons/sounds/button-3.mp3" type="audio/mp3">
    </audio>
    """

    st.markdown(sound, unsafe_allow_html=True)


# ---------------- CERTIFICATE ----------------

def create_certificate(name, score):

    file = f"{name}_certificate.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(file)

    elements = []

    elements.append(Paragraph("<h1>CERTIFICATE</h1>", styles["Heading1"]))

    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"This is to certify that", styles["Normal"]))

    elements.append(Paragraph(f"<b>{name}</b>", styles["Heading2"]))

    elements.append(Paragraph(f"Score: {score}", styles["Heading3"]))

    elements.append(Paragraph(f"Date: {datetime.now().date()}", styles["Normal"]))

    doc.build(elements)

    return file


# ---------------- LOGIN ----------------

st.title("🎓 Quiz App")

menu = st.sidebar.selectbox("Menu", ["Student", "Teacher"])


# =====================================================
# STUDENT
# =====================================================

if menu == "Student":

    name = st.text_input("Enter Your Name")

    if st.button("Start Quiz"):

        users = load_users()

        if name in users:
            st.error("❌ You already attempted")
            st.stop()

        users[name] = True
        save_users(users)

        st.session_state.name = name
        st.session_state.q = 0
        st.session_state.score = 0
        st.session_state.answers = {}



# ---------------- QUIZ ----------------

if "name" in st.session_state:

    qn = st.session_state.q

    if qn < len(questions):

        q = questions[qn]

        st.subheader(f"Question {qn+1}")

        st.write(q["question"])


        # MCQ
        if q["type"] == "mcq":

            ans = st.radio("Select", q["options"], key=qn)

            if st.button("Next"):

                if ans == q["answer"]:
                    st.session_state.score += 1

                st.session_state.q += 1
                st.rerun()



        # Writing
        if q["type"] == "write":

            text = st.text_area("Write here", key=qn)

            if st.button("Next"):

                st.session_state.answers[qn] = text
                st.session_state.q += 1
                st.rerun()



    else:

        # RESULT

        score = st.session_state.score

        st.balloons()

        play_sound()

        st.markdown(f"# 🎉 SCORE: {score}")

        # Gifts

        if score == len(questions):
            gift = "🏆 Gold Gift"

        elif score >= len(questions)//2:
            gift = "🎁 Silver Gift"

        else:
            gift = "🍫 Chocolate"

        st.markdown(f"# {gift}")


        # Save result

        results = load_results()

        results[st.session_state.name] = score

        save_results(results)


        # Certificate

        file = create_certificate(st.session_state.name, score)

        with open(file, "rb") as f:

            st.download_button(

                "Download Certificate",

                f,

                file_name=file

            )


        del st.session_state.name



# =====================================================
# TEACHER
# =====================================================

if menu == "Teacher":

    password = st.text_input("Password", type="password")

    if password == "admin123":

        st.header("📊 Live Dashboard")

        results = load_results()

        st.write(results)

        st.dataframe(

            [{"Name":k, "Score":v} for k,v in results.items()]
        )

