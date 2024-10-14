import streamlit as st
import requests
from datetime import datetime

# Title of the web app
st.title('TaxiFareModel Frontend')

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions.
''')

# Step 1: Add user input controllers
st.subheader('Input ride parameters')

# Date and time input
ride_date = st.date_input('Select ride date', datetime.today())
ride_time = st.time_input('Select ride time', datetime.now().time())

# Coordinates input
pickup_longitude = st.number_input('Pickup Longitude', format="%.6f")
pickup_latitude = st.number_input('Pickup Latitude', format="%.6f")
dropoff_longitude = st.number_input('Dropoff Longitude', format="%.6f")
dropoff_latitude = st.number_input('Dropoff Latitude', format="%.6f")

# Passenger count input
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, step=1)

# Step 2: Format the date and time
pickup_datetime = f"{ride_date} {ride_time}"

# Step 3: Build the dictionary for the API call
params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

# Step 4: Make the API call
url ='https://image-name-653722543614.europe-west1.run.app/predict'

if st.button('Get Fare Prediction'):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json().get('fare', 'No prediction returned')
        st.success(f"Estimated fare: ${prediction}")
    else:
        st.error('Error in API request!')

st.markdown('''
Once we have these, let's call our API in order to retrieve a prediction.

🤔 How could we call our API ? Off course... The `requests` package 💡
''')
