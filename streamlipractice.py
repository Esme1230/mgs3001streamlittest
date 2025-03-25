import streamlit as st
st.title("My first webapp")

# You have to write a program that determin whether you will accept loAn application or reject. You will determin acceptence based on annual salary and year of work. Acceptance standard is annual salary >= 500,000 yuan and >= 5 year of work in current work
annual_salary = st.number_input("Enter your annual salary: ")
year_work = st.number_input("Enter your year of work: ")
if st.button("Submit"):
    if annual_salary >= 5000000 and year_work >= 5:
        st.write("Your application has accepted")
else:
    st.write("Your application has rejected")