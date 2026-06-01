import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Student Marks Analyzer with Visualization")

# Input Section
name = st.text_input("Enter Student Name")
m1 = st.number_input("Enter marks for Subject 1", min_value=0, max_value=100)
m2 = st.number_input("Enter marks for Subject 2", min_value=0, max_value=100)
m3 = st.number_input("Enter marks for Subject 3", min_value=0, max_value=100)

# Calculate Button
if st.button("Calculate"):
    # Calculations
    total = m1 + m2 + m3
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display Results
    st.subheader("📋 Results")
    st.write(f"**Student Name:** {name}")
    st.write(f"**Total Marks:** {total}")
    st.write(f"**Average Marks:** {average:.2f}")

    # Highlight Grade
    if grade == "A":
        st.success(f"Grade: {grade}")
    elif grade == "B":
        st.info(f"Grade: {grade}")
    elif grade == "C":
        st.warning(f"Grade: {grade}")
    else:
        st.error(f"Grade: {grade}")

    # Data for Visualization
    data = {
        "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
        "Marks": [m1, m2, m3]
    }
    df = pd.DataFrame(data)

    # Bar Chart
    st.subheader("📊 Marks Comparison (Bar Chart)")
    st.bar_chart(df.set_index("Subjects"))

    # Line Chart
    st.subheader("📈 Marks Trend (Line Chart)")
    st.line_chart(df.set_index("Subjects"))

    # Pie Chart
    st.subheader("🥧 Marks Distribution (Pie Chart)")
    fig, ax = plt.subplots()
    ax.pie(df["Marks"], labels=df["Subjects"], autopct="%1.1f%%", startangle=90)
    ax.axis("equal")  # Equal aspect ratio ensures pie is circular
    st.pyplot(fig)

    # Table View
    st.subheader("📑 Marks Table")
    st.dataframe(df)
