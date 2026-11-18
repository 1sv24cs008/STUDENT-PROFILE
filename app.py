import streamlit as st

st.set_page_config(
    page_title="Student Profile Application",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Profile Application")
st.write("Developed by AMEER KHAN")

st.info("Fill in your details and click View My Profile.")

with st.form("student_profile_form"):

    student_name = st.text_input(
        "Student Name",
        placeholder="Enter your name"
    )

    roll_number = st.text_input(
        "USN / Roll Number",
        placeholder="Enter roll number"
    )

    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "AIDS","AIML","CX","ECE", "EEE", "ME", "Civil", "Other"]
    )

    year = st.radio(
        "Current Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    submitted = st.form_submit_button(
        "View My Profile"
    )

if submitted:

    if not student_name.strip() or not roll_number.strip():
        st.warning("Please enter all details.")

    else:
        st.success("Profile submitted successfully!")

        st.subheader("Student Profile")

        st.write("Name:", student_name)
        st.write("Roll Number:", roll_number)
        st.write("Department:", department)
        st.write("Year:", year)
