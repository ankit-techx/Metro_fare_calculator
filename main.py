# Import necessary libraries
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# Create a Tkinter window
root = Tk()
root.title("Namma Metro Fare Calculator")
root.geometry("700x680")
root.config(bg="green")

# Set window icon
image1 = ImageTk.PhotoImage(Image.open("images\download.jpg"))
root.iconphoto(False, image1)

# Create a label for the title of the application
title1 = Label(root, text="Namma Metro Fare Calculator", font=("Arial", 20), bg="green", fg="White")
title1.grid(row=0, column=0, columnspan=3)

# Create a blank label for spacing
mylabel1 = Label(root, text="        ", font=("Arial", 15), bg="green")
mylabel1.grid(row=1, column=0)

# Load and display an image for entering passengers
photo = Image.open("images\entering.jpeg")
enter_photo = ImageTk.PhotoImage(photo)
enter_photo_label = Label(image=enter_photo).grid(row=2, column=0)

# Create a label for selecting boarding station
boarding_station_label = Label(root, text="Select the boarding station", font=("Arial", 15), bg="green", fg="White")
boarding_station_label.grid(row=2, column=0)

# Create a dropdown menu for selecting boarding station
boarding_station = StringVar()
boarding_station.set("Nagasandra")
station_name = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya",
                "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road",
                "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College",
                "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road",
                "Banashankari", "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra",
                "Vajarahalli", "Thalaghattapura", "Silk Institute", "Kengeri", "Kengeri Bus Terminal", "Pattanagere",
                "Jnanabharathi", "Rajarajeshwari Nagar", "Nayandahalli", "Mysuru Road", "Deepanjali Nagara",
                "Attiguppe", "Vijayanagara", "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station",
                "Majestic", "Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha",
                "Cubbon Park Sri Chamarajendra Park", "MG Road", "Trinity", "Halasuru", "Indiranagara",
                "Swami Vivekananda Road", "Baiyappanahalli"]
boarding_station_dropdown_menu = OptionMenu(root, boarding_station, *station_name)
boarding_station_dropdown_menu.config(bg="green", fg="WHITE", height=2)
boarding_station_dropdown_menu.grid(row=2, column=1)

# Create a blank label for spacing
mylabel2 = Label(root, text="    ", font=("Arial", 15), bg="green")
mylabel2.grid(row=3, column=0)

# Load and display an image for exiting passengers
photo2 = Image.open("images\comingout.jpeg")
enter_photo1 = ImageTk.PhotoImage(photo2)
enter_photo_label1 = Label(image=enter_photo1).grid(row=4, column=0)

# Create a label for selecting departure station
departure_station_label = Label(root, text="Select the departure station", font=("Arial", 15), bg="green", fg="White")
departure_station_label.grid(row=4, column=0)

# Create a dropdown menu for selecting departure station
departure_station = StringVar()
departure_station.set("Nagasandra")
departure_station_dropdown_menu = OptionMenu(root, departure_station, *station_name)
departure_station_dropdown_menu.config(bg="green", fg="WHITE", height=2)
departure_station_dropdown_menu.grid(row=4, column=1)

# Create a blank label for spacing
mylabel3 = Label(root, text="    ", font=("Arial", 15), bg="green")
mylabel3.grid(row=5, column=0)

# Define lists of stations for Green line and Purple line
Green_line = ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya",
              "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Mahakavi Kuvempu Road",
              "Srirampura", "Sampige Road", "Majestic", "Chikpete", "Krishna Rajendra Market", "National College",
              "Lalbagh Botanical Garden", "South End Circle", "Jayanagar", "Rashtreeya Vidyalaya Road", "Banashankari",
              "Jaya Prakash Nagar", "Yelachenahalli", "Konanakunte Cross", "Doddakallasandra", "Vajarahalli",
              "Thalaghattapura", "Silk Institute"]
Purple_line = ["Kengeri", "Kengeri Bus Terminal", "Pattanagere", "Jnanabharathi", "Rajarajeshwari Nagar",
               "Nayandahalli", "Mysuru Road", "Deepanjali Nagara", "Attiguppe", "Vijayanagara",
               "Balagangadhara Natha Swamiji HOS", "Magadi Road", "City Railway Station", "Majestic",
               "Sir M. Visveshwaraya Station", "Dr BR Ambedkar Vidhana Soudha", "Cubbon Park Sri Chamarajendra Park",
               "MG Road", "Trinity", "Halasuru", "Indiranagara", "Swami Vivekananda Road", "Baiyappanahalli"]

# Define function to calculate fare
def calculate_fare():
    boarding = boarding_station.get()
    departure = departure_station.get()
    no_of_stops = 0

    # Check if boarding and departure stations are the same
    if boarding == departure:
        messagebox.showwarning("Warning", "The boarding and departure stations are the same")
        return

    # Calculate number of stops based on the lines and stations selected
    if ((boarding in Green_line and departure in Green_line) or
            (boarding in Purple_line and departure in Purple_line)):
        no_of_stops = abs(station_name.index(boarding) - station_name.index(departure)) - 1

    if (boarding in Green_line and departure in Purple_line):
        no_of_stops = abs(abs(Green_line.index("Majestic") - Green_line.index(boarding)) +
                          abs(Purple_line.index("Majestic") - Purple_line.index(departure)) - 1)

    if (boarding in Purple_line and departure in Green_line):
        no_of_stops = abs(abs(Purple_line.index("Majestic") - Purple_line.index(boarding)) +
                          abs(Green_line.index("Majestic") - Green_line.index(departure)) - 1)

    # Calculate fare based on the number of stops
    if no_of_stops == 0:
        price = 5
    elif no_of_stops == 1:
        price = 9
    elif no_of_stops == 2:
        price = 13
    elif no_of_stops == 3:
        price = 17
    else:
        price = 17 + (no_of_stops - 3) * 4

    # Display fare information in a message box
    messagebox.showinfo("Fare", f"The fare for your journey is Rs. {price}")

# Create a button to calculate fare, bind it to the calculate_fare function
calculate_button = Button(root, text="Calculate Fare", font=("Arial", 15), bg="green", fg="White",
                          command=calculate_fare)
calculate_button.grid(row=6, column=0, columnspan=3)

# Define function to exit the program
def exit_program():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        root.destroy()

# Create a button to exit the program, bind it to the exit_program function
exit_button = Button(root, text="Exit", font=("Arial", 15), bg="green", fg="White", command=exit_program)
exit_button.grid(row=7, column=0, columnspan=3)

# Start the Tkinter event loop
root.mainloop()
