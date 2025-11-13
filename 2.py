import streamlit as st
import datetime 

st.title("Hello Faizan! This is my first experience with Streamlit.")
st.text("I am Football player and i love to play football.")
st.write("Who is your favorite football player?")
player = st.selectbox("Select your favorite player:", ["Cristiano Ronaldo", "Lionel Messi", "Neymar Jr"])

if player:
    st.write("Your favorite player is: ", player)

st.write("Your choice is Good!")

st.title("Lets check what is the age of user if he ENter his DOB")

dob = st.date_input("Enter your Date of Birth",min_value=datetime.date(1900, 1, 1))
today = datetime.date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
if st.button("Calculate Age"):
    st.write("Your age is: ", age)

name = st.text_input("Enter your name:")
if name:
    st.write("Hello,", name, "Welcome your age is", age)

st.title("Lets do more practice with Streamlit")

pr = st.radio("Select your preferred programming language:", ["Python", "JavaScript", "Java", "C++"])
st.write("Your favorite programming language is: ",pr)
st.checkbox("I agree to the terms and conditions")
st.slider("Select your experience level:", 0, 10, 5)

day = st.number_input("Enter number of days you exercise in a week:", min_value=0, max_value=7, step=1)
st.write("You exercise", day, "days a week.")