import streamlit as st
import requests
import json
from PIL import Image

st.set_page_config(layout="centered", page_icon="✈️", page_title="Airline Passanger Satisfaction Predictor")
st.title("✈️ Airline Passanger Satisfaction Predictor ✈️")
st.subheader('This predict the passanger satisfaction of an airline')

image = Image.open('Header.png')
st.image(image, use_column_width = True, caption='Airline Passanger Satisfaction Predictor')

st.header("Passanger Flight Information")

col1, col2 = st.columns(2)

with col1:
    Gender = st.selectbox("Select Gender Passenger", ['Male', 'Female'])
    Customer_Type = st.selectbox("Select Customer Type", ['Loyal Customer', 'disloyal Customer'])
    Age = st.number_input("Input Age of Passenger", value=0, min_value=0, max_value=100)

with col2:
    Class = st.selectbox("Select Which Class of Flight", ['Eco Plus', 'Business', 'Eco'])
    Type_Travel = st.selectbox("Select Type of Travel", ['Personal Travel', 'Business travel'])
    Flight_distance = st.number_input("Input The Flight Distance", value=0, min_value=0, max_value=1000)


st.header("Passenger Satisfaction Rate")
st.write("**Rate the satisfaction from 1 to 5**")

col1, col2 = st.columns(2)

with col1:
    Inflight_wifi = st.selectbox("Select Satisfaction Level Inflight WiFi Rate", ['1','2','3','4','5'])
    Inflight_entertainment = st.selectbox("Select Satisfaction Level Inflight Entertainment Rate", ['1','2','3','4','5'])
    Ease_booking = st.selectbox("Select Satisfaction Level Ease of Booking Rate", ['1','2','3','4','5'])
    Checkin_service = st.selectbox("Select Satisfaction Level Ease of Checkin Rate", ['1','2','3','4','5'])
    Baggage_handling = st.selectbox("Select Satisfaction Level Baggage Handling Rate", ['1','2','3','4','5'])
    Dep_Arv_time = st.selectbox("Select Satisfaction Level of Departure/Arrival time Rate", ['1','2','3','4','5'])
    Gate_location = st.selectbox("Select Satisfaction Level of Gate Location Rate", ['1','2','3','4','5'])

with col2:
    Inflight_service = st.selectbox("Select Satisfaction Level Inflight Service Rate", ['1','2','3','4','5'])
    Seat_comfort = st.selectbox("Select Satisfaction Level Seat Comfort Rate", ['1','2','3','4','5'])
    Leg_room = st.selectbox("Select Satisfaction Level Leg Room Space Rate", ['1','2','3','4','5'])
    Cleanliness = st.selectbox("Select Satisfaction Level Cleanliness Rate", ['1','2','3','4','5'])
    Online_boarding = st.selectbox("Select Satisfaction Level Online Boarding Service Rate", ['1','2','3','4','5'])
    Onboard_service = st.selectbox("Select Satisfaction Level Onboard Service Rate", ['1','2','3','4','5'])
    Food_drink = st.selectbox("Select Satisfaction Level Food and drink rate", ['1','2','3','4','5'])


st.header("Time Flight Delay")
st.write("**Delay times in minutes (Max : 2000 min)**")
col1, col2 = st.columns(2)

with col1:
    Arrival_delay = st.number_input("Input The Arrival Delay(in minutes)", value=0, min_value = 0, max_value=2000)
    Departure_delay = st.number_input("Input The Departure Delay(in minutes)", value=0, min_value = 0, max_value=2000 )

# Inference Set
data = {'Gender' : Gender,
        'Age' : Age,
        'Customer_Type' : Customer_Type,
        'Class' : Class,
        'Type_Travel' : Type_Travel,
        'Inflight_wifi' : Inflight_wifi,
        'Ease_booking' : Ease_booking,
        'Online_boarding' : Online_boarding,
        'Seat_comfort' : Seat_comfort,
        'Inflight_entertainment' : Inflight_entertainment,
        'On-board_service' : Onboard_service,
        'Leg_room' : Leg_room,
        'Checkin_service' : Checkin_service,
        'Cleanliness' : Cleanliness,
        'Flight_distance' : Flight_distance,
        'Baggage_handling' : Baggage_handling,
        'Inflight_service' : Inflight_service,
        'Dep/Arv_time' : Dep_Arv_time,
        'Gate_location' : Gate_location,
        'Food_drink' : Food_drink,
        'Arrival_delay' : Arrival_delay,
        'Departure_delay' : Departure_delay}

URL = "https://airplane-pred.herokuapp.com/predict"



# Komunikasi
satisfaction_prediction = st.button('Predict')
if satisfaction_prediction :
    r = requests.post(URL, json=data)
    res = r.json()

    if res['code'] == 200:
        res2 = (res['result']['description'])
        if res2 == 'Not Satisfied':
            st.markdown(''' <h2> Not Satisfied </h2>''', unsafe_allow_html=True)
            col4,col5,col6 = st.columns([1,1,1])
            with col5 : 
                st.image('NotHappy.jpg')
        else:
            st.markdown(''' <h2> Satisfied </h2>''', unsafe_allow_html=True)
            col7,col8,col9 = st.columns([1,1,1])
            with col8:
                st.image('Happy.jpg')
    else:
        st.write("Error....")
        st.write(f"Details : {res['result']['error_msg']}")


prediction = st.button('Predict')
if prediction :
    r = requests.post(URL, json=data)
    res = r.json()

    if res['code'] == 200:
        rezz = (res['result']['description'])
        if rezz == 'Not Rain':
            st.markdown(''' <h2> Not Rain </h2>''', unsafe_allow_html=True)
            
        else:
            st.markdown(''' <h2> Rain </h2>''', unsafe_allow_html=True)
           
    else:
        st.write("Something Went Wrong....")
        st.write(f"Details : {res['result']['error_msg']}")