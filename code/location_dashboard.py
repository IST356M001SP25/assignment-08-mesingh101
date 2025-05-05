'''
location_dashboard.py
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

# Load data
df = pd.read_csv('./cache/tickets_in_top_locations.csv')

# Sidebar: Select location
st.sidebar.title("🎯 Select a Location")
selected_location = st.sidebar.selectbox("Choose from top ticketed locations:", sorted(df['location'].unique()))

# Filter the data
filtered = df[df['location'] == selected_location]

st.title("📍 Parking Ticket Trends by Location")
st.markdown(f"### Selected Location: `{selected_location}`")

# --- Chart 1: Tickets by Day of the Week ---
st.subheader("📅 Tickets by Day of the Week")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered, x='dayofweek', order=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], palette='Set2', ax=ax1)
ax1.set_xlabel("Day of Week")
ax1.set_ylabel("Number of Tickets")
ax1.set_title("Distribution by Day")
st.pyplot(fig1)

# --- Chart 2: Tickets by Hour of the Day ---
st.subheader("⏰ Tickets by Hour of the Day")
fig2, ax2 = plt.subplots()
sns.countplot(data=filtered, x='hourofday', palette='coolwarm', ax=ax2)
ax2.set_xlabel("Hour (0–23)")
ax2.set_ylabel("Number of Tickets")
ax2.set_title("Distribution by Hour")
st.pyplot(fig2)
