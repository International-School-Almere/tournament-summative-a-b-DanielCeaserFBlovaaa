#main file for the Tournament App.
import json         #for saving data in a JSON file
import random       #for user/team/event ID creation
import tkinter as tk
from turtle import onclick


#Global Variables:

participants_list = {} #stores individual participants and their details
teams_list = {}        #stores teams and their details
events_list = {}       #stores events and their details
results_list = {}      #stores results of events and the points awarded to participants/teams
points_system = {
    '1st': 10,
    '2nd': 8,
    '3rd': 5,
    '4th': 3,
    '5th': 1
}                 #point system used across the scoring system

#-------------------------------------------#
#Functions for participants, teams, events, and results 

def add_participant():
    name_participant = input("Enter your name: ")
    age_participant = input("Enter your age: ")
    ID_participant = participant_ID()

    participants_list.append({
        'name': name_participant,
        'age': age_participant,
        'ID': ID_participant})
    save_data() #this will save the data to the JSON file after a participant is added, this ensures that the data is not lost when the app is closed
    
def add_team():
    name_team = input("Enter your team name: ")
    members_team = input("Enter the names of team members (comma separated): ")
    ID_team = team_ID()

    teams_list.append({
        'name': name_team,
        'members': members_team,
        'ID': ID_team})

def create_event():
    name_event = input("Enter the event name: ")
    event_type = input("Is the event individual or team-based? ")
    event_category = input("Is the event based on a sport or acedemic competition? ")
    ID_event = event_ID()

    events_list.append({
        'name': name_event,
        'type': event_type,
        'category': event_category,
        'ID': ID_event})
    
def enter_results():
    event_name = input("Enter the name of the event: ") 
    participant_name = input("Enter the name of the participant/team: ") 
    position = int(input("Enter the final position (1-5): ")) 
    
    results_list.append({
        'event': event_name, 
        'participant': participant_name, 
        'position': position}) 
    
def participant_ID():
    return random.randint(1, 999)

def team_ID():
    return random.randint(1000, 1999)

def event_ID():
    return random.randint(2000, 2999)

#-------------------------------------------#
#Saving and loading data in JSON file

def save_data():
    with open('tournament_data.json', 'w') as f:
        json.dump({
            'participants': participants_list,
            'teams': teams_list,
            'events': events_list,
            'results': results_list
        }, f)

def load_data():
    global participants_list, teams_list, events_list, results_list
    try:
        with open('tournament_data.json', 'r') as f: #this will open the JSON file and load the data into the correct lists
            data = json.load(f)
            participants_list = data.get('participants', []) #data.get() is to get the data from the JSON file, if the data is not found this also ensures it does not crash
            teams_list = data.get('teams', [])
            events_list = data.get('events', [])
            results_list = data.get('results', [])
    except FileNotFoundError:
        print("No existing data found. Starting with empty lists.") #Creates clear and a user-friendly message if the data is not found, instead of for example returning back to the menu or crashing


#--------------------------------------------#
#GUI
root = tk.Tk() 
root.title("The Scoring System App")
root.geometry("1000x700") 



#-----------------------------#
#Main Frame and button functions
def show_main_frame():
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True) #Fills the entire window, expands/decreases in size with the size of the window

    # Here is where I will be creating the buttons for the main menu
    addparticipant_button = tk.Button(root, text="Add a participant", command = show_add_participant_page) 
    addparticipant_button.pack(pady=10)


    addteam_button = tk.Button(root, text="Add a team", command = show_add_team_page)
    addteam_button.pack(pady=10)


    createevent_button = tk.Button(root, text="Create an event", command = show_create_event_page) 
    createevent_button.pack(pady=10) 


    enterresults_button = tk.Button(root, text="Enter results", command = show_enter_results_page) 
    enterresults_button.pack(pady=10)


    exit_button = tk.Button(root, text="Exit", command=root.quit) 
    exit_button.pack(pady=10)

    #pack(pady=10) is used to display the buttons, where "pady" spaces them out to add structure and better visuals

#Functions 
#Add Participant page
def show_add_participant_page():
   
    entry_name = tk.Entry(root)
    entry_name.pack()
    entry_name.pack(pady=10)
    entry_name.insert(0, "Enter your name")
    entry_name.bind("<FocusIn>", onclick) #this will clear the entry box when the user clicks on it, for better structure and a more professional app
    entry_age = tk.Entry(root)
    entry_age.pack()
    entry_age.pack(pady=10)
    entry_age.insert(0, "Enter your age")
    entry_age.bind("<FocusIn>", onclick) #this will clear the entry box when the user clicks on it, for better structure and a more professional app
    submit_button = tk.Button(root, text="Submit", command=add_participant)
    submit_button.pack(pady=10)

    if onclick(submit_button) == True:
        add_participant()
        show_main_frame() #this will return the user to the main menu after they have added a participant, for better structure and a more professional app


#Add Team page
def show_add_team_page():
    clear_frame(root) 
    open 


#Create Event page
def show_create_event_page():
    clear_frame(root)
    open

#Enter Results page
def show_enter_results_page():
    clear_frame(root)
    open


#Clear Function
def clear_frame(frame):
    for widget in frame.winfo_children():   
        widget.destroy()
#This will be used to clear the previous page when a new button is clicked by the user, for better structure and a more professional app


#------------------------------#


#Start of the app
show_main_frame() #this will show the main menu when the app is started

root.mainloop() 