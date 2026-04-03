#main file for the Tournament App.
import json         #for saving data in a JSON file
import random       #for user/team/event ID creation
import tkinter as tk

#Global Variables:

participants_list = []
teams_list = []
events_list = []
results_list = []

# ---------- JSON ----------
def save_data():
    with open("tournament_data.json", "w") as f:
        json.dump({
            "participants": participants_list,
            "teams": teams_list,
            "events": events_list,
            "results": results_list
        }, f, indent=4)

#-------------------------------------------#
#Functions for participants, teams, events, and results 

def add_participant():
    name_participant = input("Enter your name: ")
    age_participant = input("Enter your age: ")
    ID_participant = participant_ID()

    participants_list.append[{
        'name': name_participant,
        'age': age_participant,
        'ID': ID_participant}]
    save_data() #this will save the data to the JSON file after a participant (but also for the other functions) is added, this ensures that the data is not lost when the app is closed
    
def add_team():
    name_team = input("Enter your team name: ")
    members_team = input("Enter the names of team members (comma separated): ")
    ID_team = team_ID()

    teams_list.append[{
        'name': name_team,
        'members': members_team,
        'ID': ID_team}]
    save_data() 

def create_event():
    name_event = input("Enter the event name: ")
    event_type = input("Is the event individual or team-based? ")
    event_category = input("Is the event based on a sport or acedemic competition? ")
    ID_event = event_ID()

    events_list.append[{
        'name': name_event,
        'type': event_type,
        'category': event_category,
        'ID': ID_event}]
    save_data()
    
def enter_results():
    event_name = input("Enter the name of the event: ") 
    participant_name = input("Enter the name of the participant/team: ") 
    position = int(input("Enter the final position (1-5): ")) 
    
    results_list.append[{
        'event': event_name, 
        'participant': participant_name, 
        'position': position}]
    save_data() 
    
def participant_ID():
    return random.randint(1, 999)

def team_ID():
    return random.randint(1000, 1999)

def event_ID():
    return random.randint(2000, 2999)



#--------------------------------------------#
#GUI
root = tk.Tk() 
root.title("The Scoring System App")
root.geometry("1000x700") 

#-----------------------------#
#Main Frame 
def main_frame():
    clear_frame(root)
    tk.Label(main_frame, text="Tournament System", font=("Arial", 20)).pack(pady=20)
    
    
#Functions 
def onclick(removal):
    removal.delete(0, tk.END) #this will clear the entry box when the user clicks on it, for better structure and a more professional app
    return True #this will return to the show_add_participant_page function, which will then use the add_participant function, this is used to ensure that the participant is added after the user has entered their details and clicked submit
  

#Add Participant page
def add_participant_page():
    clear_frame(root)
    tk.Label(root, text="Add a Participant", font=("Arial", 20)).pack(pady=20)
   
    entry_name = tk.Entry(main_frame)
    entry_name.pack(pady=10)
    entry_name.insert(0, "Enter your name")
    entry_name.bind("<FocusIn>", onclick) #this will clear the entry box when the user clicks on it, for better structure and a more professional app
    
    entry_age = tk.Entry(main_frame)
    entry_age.pack()
    entry_age.pack(pady=10)
    entry_age.insert(0, "Enter your age")
    entry_age.bind("<FocusIn>", onclick) #this will clear the entry box when the user clicks on it, for better structure and a more professional app
    
    result_laber = tk.Label(main_frame, text="")
    result_laber.pack(pady=5)

    def submit():
        pid=participant_ID()

        participants_list.append({
            'name': entry_name.get(),
            'age': entry_age.get(),
            'ID': pid})
        save_data() #this will save the data to the JSON file after a participant is added
        result_laber.config(text=f"Participant added with ID: {pid}") #this will show the user that the participant has been added and display their ID
    submit_button = tk.Button(main_frame, text="Submit", command=submit)
    submit_button.pack(pady=5)
#Add Team page
def add_team_page():
    clear_frame(root) 
    open 


#Create Event page
def create_event_page():
    clear_frame(root)
    open

#Enter Results page
def enter_results_page():
    clear_frame(root)
    open


#Clear Function
def clear_frame(frame):
    for widget in frame.winfo_children():   
        widget.destroy()
#This will be used to clear the previous page when a new button is clicked by the user, for better structure and a more professional app


#------------------------------#
#Menu Buttons 

tk.Label(root, text="Welcome to the Tournament Scoring System", font=("Arial", 20)).pack(pady=20) #this is the title of the app, it will be displayed at the top of the main menu

tk.Button(main_frame, text="Add Participant", command=add_participant).pack(side="left", padx=5)
tk.Button(main_frame, text="Add Team", command=add_team).pack(side="left", padx=5)
tk.Button(main_frame, text="Create Event", command=create_event).pack(side="left", padx=5)
tk.Button(main_frame, text="Enter Results", command=enter_results).pack(side="left", padx=5)
tk.Button(main_frame, text="Exit", command=root.quit).pack(side="right", padx=5)

#Start of the app
main_frame() #this will show the main menu when the app is started

root.mainloop() 