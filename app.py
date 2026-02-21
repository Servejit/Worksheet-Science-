import streamlit as st
import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Class 10 Light Exam", layout="centered")

DATA_FILE = "class10_light_students.json"

# ---------- Load Data ----------

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

with open(DATA_FILE, "r") as f:
    students = json.load(f)

# ---------- MCQs WITHOUT ANSWERS ----------

questions = [

("Image formed by plane mirror is:", ["Real","Virtual","Both","None"]),

("Concave mirror is:", ["Converging","Diverging","Both","None"]),

("Convex mirror is:", ["Converging","Diverging","Both","None"]),

("Unit of focal length:", ["cm","m","Both","None"]),

("Mirror formula is:", ["1/f = 1/v + 1/u","f = uv","v = u","None"]),

("SI unit of distance:", ["cm","mm","m","None"]),

("Centre of mirror is:", ["Pole","Focus","Centre of curvature","None"]),

("Middle point of mirror:", ["Pole","Focus","Radius","None"]),

("Parallel rays meet at:", ["Focus","Pole","Centre","None"]),

("Convex mirror image always:", ["Real","Virtual","Both","None"]),

("Concave mirror image can be:", ["Real","Virtual","Both","None"]),

("Focal length is half of:", ["Diameter","Radius","Pole","None"]),

("Image distance is represented by:", ["u","v","f","None"]),

("Object distance is represented by:", ["u","v","f","None"]),

("Focal length represented by:", ["u","v","f","None"]),

("Real image is:", ["Inverted","Erect","Both","None"]),

("Virtual image is:", ["Inverted","Erect","Both","None"]),

("Convex mirror used in:", ["Rear view mirror","Torch","Microscope","None"]),

("Concave mirror used in:", ["Torch","Rear view mirror","Both","None"]),

("Mirror obeys:", ["Reflection","Refraction","Both","None"]),

("Angle of incidence equals:", ["Angle of reflection","Angle of refraction","Both","None"]),

("Mirror formula works for:", ["All mirrors","Only concave","Only convex","None"]),

("Pole lies on:", ["Mirror surface","Behind mirror","Front","None"]),

("Focus lies between:", ["Pole and centre","Centre and infinity","None","None"]),

("Convex mirror forms image:", ["Small","Large","Same","None"]),

]

# ---------- ANSWER KEY (Hidden) ----------

answer_key = [

"Virtual",
"Converging",
"Diverging",
"Both",
"1/f = 1/v + 1/u",
"m",
"Centre of curvature",
"Pole",
"Focus",
"Virtual",
"Both",
"Radius",
"v",
"u",
"f",
"Inverted",
"Erect",
"Rear view mirror",
"Torch",
"Reflection",
"Angle of reflection",
"All mirrors",
"Mirror surface",
"Pole and centre",
"Small"

]

# ---------- Numericals ----------

numericals = [

"Object distance = -20 cm, focal length = -10 cm. Find image distance.",

"Image distance = 30 cm, focal length = 15 cm. Find object distance.",

"Object distance = -30 cm, image distance = -60 cm. Find focal length.",

"Focal length = 20 cm, object distance = -40 cm. Find image distance.",

"Image distance = 40 cm, focal length = 10 cm. Find object distance."

]

# ---------- Certificate ----------

def create_certificate(name, score):

    filename = f"{name}_Certificate.pdf"

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>CERTIFICATE OF ACHIEVEMENT</b>", styles["Title"]))
    story.append(Spacer(1,20))
    story.append(Paragraph(f"Student: {name}", styles["Normal"]))
    story.append(Paragraph(f"Score: {score}/25", styles["Normal"]))

    doc.build(story)

    return filename

# ---------- UI ----------

st.title("Class 10 Science – Light")

name = st.text_input("Student Name")

if name in students:

    st.error("Already attempted")

    st.stop()

answers = []

for i,q in enumerate(questions):

    st.write(f"{i+1}. {q[0]}")

    ans = st.radio("", q[1], key=i)

    answers.append(ans)

st.header("Numericals")

for n in numericals:

    st.text_area(n)

# ---------- Submit ----------

if st.button("Submit"):

    score = 0

    for i in range(len(answer_key)):

        if answers[i] == answer_key[i]:

            score += 1

    students[name] = score

    with open(DATA_FILE,"w") as f:

        json.dump(students,f)

    st.success(f"Score: {score}/25")

    file = create_certificate(name, score)

    with open(file,"rb") as f:

        st.download_button("Download Certificate", f, file_name=file)

# ---------- Teacher ----------

st.sidebar.title("Teacher")

if st.sidebar.checkbox("Results"):

    for s in students:

        st.sidebar.write(s, students[s])
