# ---------------------------------------------------
# INSTALL (Run once in terminal)
# pip install streamlit
# ---------------------------------------------------

import streamlit as st
import base64

st.set_page_config(page_title="Sample Worksheet", layout="wide")

# ---------------------------------------------------
# SOFT SOUND (Base64 small beep)
# ---------------------------------------------------

wrong_sound = """
<audio autoplay>
<source src="data:audio/wav;base64,UklGRigAAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQgAAAAA" type="audio/wav">
</audio>
"""

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📘 Sample Worksheet")
st.write("### Class VI – Science")

# ---------------------------------------------------
# STUDENT INFO
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")

with col2:
    student_class = st.text_input("Class")

st.divider()

# ---------------------------------------------------
# ANSWERS
# ---------------------------------------------------

correct_answers = {
    "mcq1": "Poles",
    "mcq2": "Sedimentary",
    "mcq3": "Sun",
    "fill1": "artificial",
    "fill2": "transpiration",
    "fill3": "compass"
}

score = 0
max_score = 10


# ---------------------------------------------------
# SECTION A MCQ
# ---------------------------------------------------

st.subheader("Section A – MCQ")

mcq1 = st.radio(
    "1. Magnetic strength maximum at:",
    ["Centre", "Poles", "Corners", "Same throughout"],
    key="mcq1"
)

if mcq1:
    if mcq1 == correct_answers["mcq1"]:
        st.success("✔ Correct")
    else:
        st.error("✘ Wrong")
        st.markdown(wrong_sound, unsafe_allow_html=True)


mcq2 = st.radio(
    "2. Fossils found in:",
    ["Igneous", "Sedimentary", "Metamorphic", "Any"],
    key="mcq2"
)

if mcq2:
    if mcq2 == correct_answers["mcq2"]:
        st.success("✔ Correct")
    else:
        st.error("✘ Wrong")
        st.markdown(wrong_sound, unsafe_allow_html=True)


mcq3 = st.radio(
    "3. Ultimate source of energy:",
    ["Water", "Air", "Fossil fuels", "Sun"],
    key="mcq3"
)

if mcq3:
    if mcq3 == correct_answers["mcq3"]:
        st.success("✔ Correct")
    else:
        st.error("✘ Wrong")
        st.markdown(wrong_sound, unsafe_allow_html=True)


# ---------------------------------------------------
# FILL UPS
# ---------------------------------------------------

st.subheader("Section B – Fill in the blanks")

fill1 = st.text_input("4. Horseshoe magnets are ______ magnets")

if fill1:
    if fill1.lower() == correct_answers["fill1"]:
        st.success("✔ Correct")
    else:
        st.error("✘ Wrong")


fill2 = st.text_input("5. Loss of water through leaves is ______")

if fill2:
    if fill2.lower() == correct_answers["fill2"]:
        st.success("✔ Correct")
    else:
        st.error("✘ Wrong")


fill3 = st.text_input("6. Instrument to find direction is ______")

if fill3:
    if fill3.lower() == correct_answers["fill3"]:
        st.success("✔ Correct")
    else:
        st.error("✘ Wrong")


# ---------------------------------------------------
# WRITING SPACE
# ---------------------------------------------------

st.subheader("Section C – Short Answers")

ans7 = st.text_area("7. What is evaporation?", height=120)

ans8 = st.text_area("8. What are meteorites?", height=120)


st.subheader("Section D – Long Answer")

ans9 = st.text_area("9. How clouds are formed?", height=150)


st.subheader("Section E – HOTS")

ans10 = st.text_area("10. Why natural magnets not used in cranes?", height=120)


# ---------------------------------------------------
# SUBMIT BUTTON
# ---------------------------------------------------

if st.button("Submit Worksheet"):

    score = 0

    if mcq1 == correct_answers["mcq1"]:
        score += 1

    if mcq2 == correct_answers["mcq2"]:
        score += 1

    if mcq3 == correct_answers["mcq3"]:
        score += 1

    if fill1.lower() == correct_answers["fill1"]:
        score += 1

    if fill2.lower() == correct_answers["fill2"]:
        score += 1

    if fill3.lower() == correct_answers["fill3"]:
        score += 1


    # Convert to score out of 10
    final_score = round((score / 6) * 10, 2)

    st.divider()

    st.success(f"🎉 Submitted Successfully!")

    st.write("### Student Details")

    st.write(f"Name: {name}")
    st.write(f"Class: {student_class}")

    st.write("## 🏆 Score:", final_score, "/ 10")
      
