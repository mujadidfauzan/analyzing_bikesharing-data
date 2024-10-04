import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

# Set page configuration
st.set_page_config(
    page_title="Bike Rental",
    page_icon=":bike:",
    layout="wide"
)

# Set title and caption
st.title('Bike Rental Dashboard')
st.caption('Mujadid Fauzan Salim Tamin')

# Load data function
def load_data(path: str):
    data = pd.read_csv(path)
    # Change 'dteday' to datetime
    data['dteday'] = pd.to_datetime(data['dteday'])
    return data

# Load dataset
df = load_data('./dashboard/hour.csv')  # Update this path to your CSV file

# Create dictionary for months
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

# Select month with month names as options
month_selection = st.sidebar.selectbox(
    'Select Month:',
    list(months.values())  # Display month names
)

# Get the month number based on selection
selected_month_number = list(months.keys())[list(months.values()).index(month_selection)]

# Filter data based on selected month
output = df[df['mnth'] == selected_month_number]

#-----USER METRICS-----#
col1, col2, col3 = st.columns(3)

with col1:
    total_cnt = output['cnt'].sum()
    st.metric("Total Rental", total_cnt)

with col2:
    total_registered = output['registered'].sum()
    st.metric("Registered User", total_registered)

with col3:
    total_casual = output['casual'].sum()
    st.metric("Casual User", total_casual)

# Style metric cards
style_metric_cards(border_left_color="#F08080")
st.divider()

# Plot the relationship between hours and bike rentals
st.subheader('Relationship between Hour and Number of Bike Rentals')

plt.figure(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=output)  # Adjust for selected month

plt.xticks(ticks=range(0, 24), labels=range(0, 24))  # Set x-ticks for hours

plt.title('Hubungan antara Jam dan Jumlah Penyewaan Sepeda')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan Sepeda')

plt.tight_layout()
st.pyplot(plt)

# Plot: Heatmap of bike rentals by hour and day of the week
st.subheader('Heatmap of Bike Rentals by Hour and Day of the Week')

# Create a pivot table for the heatmap
heatmap_data = df.pivot_table(index='hr', columns='weekday', values='cnt', aggfunc='sum')

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g')

plt.title('Heatmap of Bike Rentals')
plt.xlabel('Day of the Week')
plt.ylabel('Hour of the Day')

plt.xticks(ticks=np.arange(7) + 0.5, labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])  # Labels for days

plt.tight_layout()
st.pyplot(plt)

# Plot: Distribution of bike rentals
st.subheader('Distribution of Bike Rentals')

plt.figure(figsize=(12, 6))
sns.histplot(output['cnt'], bins=30, kde=True)  # Using the filtered output for the selected month

plt.title('Distribusi Jumlah Penyewaan Sepeda')
plt.xlabel('Jumlah Penyewaan Sepeda')
plt.ylabel('Frekuensi')

plt.tight_layout()
st.pyplot(plt)

# Plot: Bar plot for bike rentals by season
st.subheader('Jumlah Penyewaan Sepeda Berdasarkan Musim')

plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=df, palette='viridis')  # Using the entire dataset for season plot

plt.title('Jumlah Penyewaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Spring', 'Summer', 'Fall', 'Winter'])  # Labeling seasons

plt.tight_layout()
st.pyplot(plt)
