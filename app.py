
import streamlit as st

st.title("DERIVATIVE DEFENDER")
st.write("Welcome to the Calculus Adventure!")

st.subheader("CHOOSE YOUR AGENT")

agent = st.selectbox(
    "Select your agent:",
    ["Vector", "Nova", "Cipher", "Blaze", "Echo"]
)

st.write("Your agent is:", agent)

st.subheader("MISSION 1: ESCAPE THE BRIDGE")

st.write("Given: s(t) = t² + 3t")
st.write("Find the velocity when t = 2.")

answer = st.radio(
    "Choose the correct gate:",
    ["5 m/s", "7 m/s", "9 m/s"]
)

if st.button("ENTER GATE"):
    if answer == "7 m/s":
        st.success("Correct! You survived!")
        st.balloons()
    else:
        st.error("Wrong gate! You lost health.")
