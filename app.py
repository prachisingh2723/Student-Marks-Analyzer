import streamlit as st
import pandas as pd

# App Title
st.title("📊 Student Marks Analyzer with Visualization")

# Input Section
name = st.text_input("Enter Student Name")

subject1 = st.number_input(
    "Enter Marks for Subject 1",
    min_value=0,
    max_value=100
)

subject2 = st.number_input(
    "Enter Marks for Subject 2",
    min_value=0,
    max_value=100
)

subject3 = st.number_input(
    "Enter Marks for Subject 3",
    min_value=0,
    max_value=100
)

# Calculate Results
if st.button("Calculate"):

    total_marks = subject1 + subject2 + subject3
    average_marks = total_marks / 3

    # Grade Calculation
    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display Results
    st.subheader("📋 Results")
    st.write(f"Student Name: {name}")
    st.write(f"Total Marks: {total_marks}")
    st.write(f"Average Marks: {average_marks:.2f}")
    st.write(f"Grade: {grade}")

    # Create DataFrame
    marks_data = {
        "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
        "Marks": [subject1, subject2, subject3]
    }

    df = pd.DataFrame(marks_data)

    # Bar Chart
    st.subheader("📊 Marks Comparison (Bar Chart)")
    st.bar_chart(df.set_index("Subjects"))

    # Line Chart
    st.subheader("📈 Marks Trend (Line Chart)")
    st.line_chart(df.set_index("Subjects"))

    # Table View
    st.subheader("📑 Marks Table")
    st.dataframe(df)
