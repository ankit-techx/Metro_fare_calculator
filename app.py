# Import necessary libraries
import streamlit as st
from PIL import Image

# Load background image
background_image = Image.open("images/background.png")
st.image(background_image, use_column_width=True)

# Define the list of station names
station_name = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya",
                "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road",
                "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market",
                "National College", "Lalbagh Botanical Garden", "South End Circle", "Jayanagar",
                "Rashtreeya Vidyalaya Road", "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli",
                "Konanakunte Cross", "Doddakallasandra", "Vajarahalli", "Thalaghattapura", "Silk Institute",
                "Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar",
                "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara",
                "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic",
                "Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park",
                "MG Road", "Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]

# Define function to calculate fare
def calculate_fare(boarding_station, departure_station):
    Green_line = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya",
                  "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road",
                  "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College",
                  "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road",
                  "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra",
                  "Vajarahalli", "Thalaghattapura", "Silk Institute"]

    Purple_line = ["Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar",
                   "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara",
                   "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic",
                   "Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park",
                   "MG Road", "Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]

    # Check if boarding and departure stations are the same
    if boarding_station == departure_station:
        return 0, []

    # Calculate fare based on the lines and stations selected
    if boarding_station in Green_line and departure_station in Green_line:
        no_of_stops = abs(station_name.index(boarding_station) - station_name.index(departure_station)) - 1

    elif boarding_station in Purple_line and departure_station in Purple_line:
        no_of_stops = abs(station_name.index(boarding_station) - station_name.index(departure_station)) - 1

    elif boarding_station in Green_line and departure_station in Purple_line:
        no_of_stops = abs(Green_line.index("Majestic") - Green_line.index(boarding_station)) \
                      + abs(Purple_line.index("Majestic") - Purple_line.index(departure_station)) - 1

    else:  # departure_station in Green_line and boarding_station in Purple_line
        no_of_stops = abs(Purple_line.index("Majestic") - Purple_line.index(boarding_station)) \
                      + abs(Green_line.index("Majestic") - Green_line.index(departure_station)) - 1

    # Calculate fare based on the number of stops
    if no_of_stops <= 1:
        price = 10
    elif no_of_stops == 2:
        price = 15
    elif no_of_stops == 3:
        price = 18
    else:
        price = 18 + (no_of_stops - 3) * 4

    return price, station_name[min(station_name.index(boarding_station), station_name.index(departure_station)):
                               max(station_name.index(boarding_station), station_name.index(departure_station)) + 1]

# Streamlit interface
st.title("Namma Metro Fare Calculator")

# Select boarding and departure stations
boarding_station = st.selectbox("Select the boarding station", station_name)
departure_station = st.selectbox("Select the departure station", station_name)

# Calculate fare when button is clicked
if st.button("Calculate Fare"):
    fare, route = calculate_fare(boarding_station, departure_station)

    if fare == 0:
        st.warning("The boarding and departure stations cannot be the same.")
    else:
        st.info(f"The fare for your journey is Rs. {fare}")

        # Display metro route map
        st.subheader("Metro Route Map")
        st.write(route)
