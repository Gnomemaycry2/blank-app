import streamlit as st
import random

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Generate random altitude and distance
altitude = random.randint(300, 3000)
distance = random.randint(500, 12000)

st.header("Random Values")
col1, col2 = st.columns(2)

with col1:
    st.metric("Altitude", f"{altitude} m")

with col2:
    st.metric("Distance", f"{distance} m")
