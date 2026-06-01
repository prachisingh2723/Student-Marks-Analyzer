```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Student Marks Analyzer",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 Student Marks Analyzer")
st.markdown("Analyze student performance with grades and visual reports.")

# Input Section
st.header("📝 Enter Student Details")

student_name = st.text_input("Student Name")

col1, col2, col3 = st.columns(3)

with col1:
    subject1 = st.number_input(
        "Subject 1 Marks",
        min_value=0,
        max_value=100,
        value=0
    )

with col2:
    subject2 = st.number_input(
        "Subject 2 Marks",
        min_value=0,
        max_value=100,
        value=0
    )

with col3:
    subject3 = st.number_input(
        "Subject 3 Marks",
        min_value=0,
        max_value=100,
        value=0
    )

# Grade Criteria
with st.expander("📖 Grade Criteria"):
    st.write("""
    - **A Grade:** 90 and above
    - **B Grade:** 75 - 89
    - **C Grade:** 50 - 74
    - **Fail:** Below 50
    """)

# Calculate Results
if st.button("Calculate Result"):

    if not student_name.strip():
        st.error("Please enter the student name.")
    else:
        # Calculations
        total_marks = subject1 + subject2 + subject3
        average_marks = total_marks / 3
        percentage = (total_marks / 300) * 100

        # Grade Determination
        if average_marks >= 90:
            grade = "A"
            performance = "Excellent Performance! 🌟"
        elif average_marks >= 75:
            grade = "B"
            performance = "Good Job! 👍"
        elif average_marks >= 50:
            grade = "C"
            performance = "Average Performance. Keep Improving!"
        else:
            grade = "Fail"
            performance = "Needs Improvement."

        # Results Section
        st.header("📋 Result Summary")

        st.write(f"**Student Name:** {student_name}")
        st.write(f"**Total Marks:** {total_marks}/300")
        st.write(f"**Average Marks:** {average_marks:.2f}")
        st.write(f"**Percentage:** {percentage:.2f}%")

        # Grade Display
        if grade == "A":
            st.success(f"Grade: {grade}")
        elif grade == "B":
            st.info(f"Grade: {grade}")
        elif grade == "C":
            st.warning(f"Grade: {grade}")
        else:
            st.error(f"Grade: {grade}")

        st.write(f"**Performance:** {performance}")

        # Data Preparation
        marks_data = pd.DataFrame({
            "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
            "Marks": [subject1, subject2, subject3]
        })

        # Statistics
        st.subheader("📈 Statistics")
        st.write(f"Highest Marks: {marks_data['Marks'].max()}")
        st.write(f"Lowest Marks: {marks_data['Marks'].min()}")

        # Bar Chart
        st.subheader("📊 Marks Comparison")
        st.bar_chart(marks_data.set_index("Subjects"))

        # Line Chart
        st.subheader("📉 Marks Trend")
        st.line_chart(marks_data.set_index("Subjects"))

        # Pie Chart
        st.subheader("🥧 Marks Distribution")

        fig, ax = plt.subplots(figsize=(5, 5))
        colors = ["#ff9999", "#66b3ff", "#99ff99"]

        ax.pie(
            marks_data["Marks"],
            labels=marks_data["Subjects"],
            autopct="%1.1f%%",
            startangle=90,
            colors=colors
        )

        ax.axis("equal")
        st.pyplot(fig)

        # Data Table
        st.subheader("📑 Marks Table")
        st.dataframe(marks_data, use_container_width=True)

        # Download Report
        report = pd.DataFrame({
            "Student Name": [student_name],
            "Subject 1": [subject1],
            "Subject 2": [subject2],
            "Subject 3": [subject3],
            "Total": [total_marks],
            "Average": [round(average_marks, 2)],
            "Percentage": [round(percentage, 2)],
            "Grade": [grade]
        })

        csv = report.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Report",
            data=csv,
            file_name="student_report.csv",
            mime="text/csv"
        )
```
