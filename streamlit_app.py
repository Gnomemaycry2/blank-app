import streamlit as st
import random
import math

st.title("Vertical angle trainer v1.2")


# Initialize session state for altitude and distance
if 'altitude' not in st.session_state:
    st.session_state.altitude = random.randint(300, 3000)
    st.session_state.distance = random.randint(500, 12000)
    st.session_state.guess_made = False

# Generate random altitude and distance
altitude = st.session_state.altitude
distance = st.session_state.distance

#st.header("Random Values")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Altitude", f"{altitude} m")

with col2:
    st.metric("Distance", f"{distance} m")

with col3:
    def reset_slider():
        st.session_state.angle = 0.0
    # Reset button
    if st.button("🔄 Reset & New Values", on_click=reset_slider, shortcut='Space'):
        st.session_state.altitude = random.randint(300, 3000)
        st.session_state.distance = random.randint(500, 12000)
        st.session_state.guess_made = False
        manual_angle = 0.0
        st.rerun()

# Calculate vertical angle
vertical_angle_rad = math.atan(altitude / distance)
vertical_angle_deg = math.degrees(vertical_angle_rad) 
vertical_angle_deg = 0 if vertical_angle_deg is None else vertical_angle_deg 

# Manual input and comparison
#st.header("Manual Input & Comparison")
manual_angle = st.number_input("Enter your vertical angle (degrees):", value=None, step=1, key='angle')

if manual_angle != 0.0:
    st.session_state.guess_made = True
    
    #st.header("Calculated Angle")
    #st.metric("Vertical Angle to Point", f"{vertical_angle_deg:.0f}°")
    
    difference = abs(manual_angle - (vertical_angle_deg + 0))
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Your Angle", f"{manual_angle:.0f}°")
    
    with col2:
        st.metric("Calculated Angle", f"{vertical_angle_deg:.0f}°")
    
    with col3:
        st.metric("Difference", f"{difference:.0f}°")
    
    # Show accuracy percentage
    accuracy = max(0, 100 - (difference / vertical_angle_deg * 100)) if vertical_angle_deg > 0 else 100
    
    if difference < 1:
        st.success(f"✅ Great! Your angle is very close. Accuracy: {accuracy:.0f}%")
    elif difference < 5:
        st.info(f"⚠️ Good attempt! Accuracy: {accuracy:.0f}%")
    else:
        st.warning(f"❌ Try again! Accuracy: {accuracy:.0f}%")


