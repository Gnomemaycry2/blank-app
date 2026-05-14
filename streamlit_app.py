import streamlit as st
import random
import math

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Initialize session state for altitude and distance
if 'altitude' not in st.session_state:
    st.session_state.altitude = random.randint(300, 3000)
    st.session_state.distance = random.randint(500, 12000)

# Generate random altitude and distance
altitude = st.session_state.altitude
distance = st.session_state.distance

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

# Manual input and comparison
st.header("Manual Input & Comparison")
manual_angle = st.number_input("Enter your vertical angle (degrees):", value=0.0, step=0.1)

if manual_angle != 0.0:
    difference = abs(manual_angle - vertical_angle_deg)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Your Angle", f"{manual_angle:.2f}°")
    
    with col2:
        st.metric("Calculated Angle", f"{vertical_angle_deg:.2f}°")
    
    with col3:
        st.metric("Difference", f"{difference:.2f}°")
    
    # Show accuracy percentage
    accuracy = max(0, 100 - (difference / vertical_angle_deg * 100)) if vertical_angle_deg > 0 else 100
    
    if difference < 1:
        st.success(f"✅ Great! Your angle is very close. Accuracy: {accuracy:.1f}%")
    elif difference < 5:
        st.info(f"⚠️ Good attempt! Accuracy: {accuracy:.1f}%")
    else:
        st.warning(f"❌ Try again! Accuracy: {accuracy:.1f}%")

# Reset button
if st.button("🔄 Reset & New Values"):
    st.session_state.altitude = random.randint(300, 3000)
    st.session_state.distance = random.randint(500, 12000)
    st.rerun()
