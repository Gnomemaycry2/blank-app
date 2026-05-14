import streamlit as st
import random
import math

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

# Calculate vertical angle
vertical_angle_rad = math.atan(altitude / distance)
vertical_angle_deg = math.degrees(vertical_angle_rad)

st.header("Calculated Angle")
st.metric("Vertical Angle to Point", f"{vertical_angle_deg:.2f}°")
