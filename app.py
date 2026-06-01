import streamlit as st
import pandas as pd
 
st.title("Student Marks Analyzer with Visualization")
 
name = st.text_input("Enter Student Name")
 
m1 = st.number_input("Enter marks for Subject 1", min_value=0, max_value=100)
m2 = st.number_input("Enter marks for Subject 2", min_value=0, max_value=100)
m3 = st.number_input("Enter marks for Subject 3", min_value=0, max_value=100)
 
if st.button("Calculate"):
   total = m1 + m2 + m3
   average = total / 3
 
   if average >= 90:
       grade ="A"
   elif average >= 75:
       grade ="B"
   elif average >= 50:
       grade ="C"
   else:
       grade ="Fail"
 
   # Display Results
   st.subheader("Results")
   st.write(f"Student Name: {name}")
   st.write(f"Total Marks: {total}")
   st.write(f"Average Marks: {average}")
   st.write(f"Grade: {grade}")
 
   # Create Data for Visualization
   data = {
       "Subjects": ["Subject 1", "Subject 2", "Subject 3"],
       "Marks": [m1, m2, m3]
   }
 
   df = pd.DataFrame(data)
 
   # Bar Chart
   st.subheader("Marks Comparison (Bar Chart)")
   st.bar_chart(df.set_index("Subjects"))
 
   # Line Chart
   st.subheader("Marks Trend (Line Chart)")
   st.line_chart(df.set_index("Subjects"))
 
   # Table View
   st.subheader("Marks Table")
   st.dataframe(df) 
