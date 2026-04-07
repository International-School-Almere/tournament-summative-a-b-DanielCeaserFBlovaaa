#main file for the Tournament App.
import json         #for saving data in a JSON file
import random       #for user/team/event ID creation
import tkinter as tk

#Global Variables:

participants_list = []
teams_list = []
events_list = []
results_list = []

point_system = {
    1: 10,
    2: 8,
    3: 6,
    4: 4,
    5: 2
}


# ---------- JSON ----------
def save_data():
    with open("tournament_data.json", "r") as f:
        data = json.load(f)
    data["participants"] = participants_list
    data["teams"] = teams_list
    data["events"] = events_list
    data["results"] = results_list
    with open("tournament_data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    global participants_list, teams_list, events_list, results_list
    try:
        with open("tournament_data.json", "r") as f:
            data = json.load(f)
            participants_list = data.get("participants", [])
            teams_list = data.get("teams", [])
            events_list = data.get("events", [])
            results_list = data.get("results", [])
    except FileNotFoundError:
        with open("tournament_data.json", "w") as f:
            json.dump({
                "participants": [],
                "teams": [],
                "events": [],
                "results": []
            }, f, indent=4)

#-------------------------------------------#
#Functions for participants, teams, events, and results and home page
def show_home():
    clear_frame(main_frame)

    tk.Label(main_frame, text="Tournament System", font=("Arial", 20)).pack(pady=20)

    tk.Button(main_frame, text="Add Participant", command=add_participant_page).pack(side="left", padx=5)
    tk.Button(main_frame, text="Add Team", command=add_team_page).pack(side="left", padx=5)
    tk.Button(main_frame, text="Create Event", command=create_event_page).pack(side="left", padx=5)
    tk.Button(main_frame, text="Enter Results", command=enter_results_page).pack(side="left", padx=5)
    tk.Button(main_frame, text="Exit", command=root.quit).pack(side="right", padx=5)


def add_participant():
    name_participant = input("Enter your name: ")
    age_participant = input("Enter your age: ")
    ID_participant = participant_ID()

    participants_list.append({
        'name': name_participant,
        'age': age_participant,
        'ID': ID_participant})
    save_data() #this will save the data to the JSON file after a participant (but also for the other functions) is added, this ensures that the data is not lost when the app is closed
    
def add_team():
    name_team = input("Enter your team name: ")
    members_team = input("Enter the names of team members (comma separated): ")
    ID_team = team_ID()

    teams_list.append({
        'name': name_team,
        'members': members_team,
        'ID': ID_team})
    save_data() 

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
    save_data()
    
def enter_results():
    event_name = input("Enter the name of the event: ") 
    participant_name = input("Enter the name of the participant/team: ") 
    position = int(input("Enter the final position (1-5): ")) 
    
    results_list.append({
        'event': event_name, 
        'participant': participant_name, 
        'position': position})
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

main_frame = tk.Frame(root)
main_frame.pack(pady=20)
tk.Label(main_frame, text="Tournament System", font=("Arial", 20)).pack(pady=20)
    
    
#Functions 
def onclick(removal):
    removal.delete(0, tk.END) #this will clear the entry box when the user clicks on it, for better structure and a more professional app
    return True #this will return to the show_add_participant_page function, which will then use the add_participant function, this is used to ensure that the participant is added after the user has entered their details and clicked submit
  

#Add Participant page
def add_participant_page():
    clear_frame(main_frame)
    tk.Label(main_frame, text="Add a Participant", font=("Arial", 20)).pack(pady=20)
    tk.Label(main_frame, text="Please remember your participant ID, as you will need it for more.").pack(pady=5)
   
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
        tk.Label(main_frame, text=f"Your participant ID is: {pid}, you have successfully entered the tournament!").pack(pady=5) #this will show the user their participant ID after they have clicked submit, this is important as they will need it for more
        tk.Button(main_frame, text="Return to Home", command=show_home).pack(pady=5) #this will return the user to the home page after they have added a participant


    submit_button = tk.Button(main_frame, text="Submit", command=submit)
    submit_button.pack(pady=5)
    
#Add Team page
def add_team_page():
    clear_frame(main_frame)
    tk.Label(main_frame, text="Add a Team", font=("Arial", 20)).pack(pady=20)
    tk.Label(main_frame, text="Please remember your team ID, as you will need it for more.").pack(pady=5)

    entry_name = tk.Entry(main_frame)
    entry_name.pack(pady=10)
    entry_name.insert(0, "Enter your team name")
    entry_name.bind("<FocusIn>", onclick) #this will clear the entry box when the user clicks on it, for better structure and a more professional app
    
    entry_contactperson = tk.Entry(main_frame)
    entry_contactperson.pack()
    entry_contactperson.pack(pady=10)
    entry_contactperson.insert(0, "Enter the name of the contact person for the team")
    entry_contactperson.bind("<FocusIn>", onclick) 

    entry_contactdetails = tk.Entry(main_frame)
    entry_contactdetails.pack()
    entry_contactdetails.pack(pady=10)
    entry_contactdetails.insert(0, "Enter the email address of the contact person for the team")
    entry_contactdetails.bind("<FocusIn>", onclick)

    result_laber = tk.Label(main_frame, text="")
    result_laber.pack(pady=5)

    def submit():
        tid=team_ID()
        

        teams_list.append({
            'teamname': entry_name.get(),
            'contactperson': entry_contactperson.get(),
            'contactdetails': entry_contactdetails.get(),
            'teamID': tid})
        save_data() #this will save the data to the JSON file after a team is added
        tk.Label(main_frame, text=f"Your team ID is: {tid}, you have successfully entered the tournament!").pack(pady=5) #this will show the user their team ID after they have clicked submit, this is important as they will need it for more
        tk.Button(main_frame, text="Return to Home", command=show_home).pack(pady=5) #this will return the user to the home page after they have added a team


    submit_button = tk.Button(main_frame, text="Submit", command=submit)
    submit_button.pack(pady=5)


#Create Event page
def create_event_page():
    clear_frame(main_frame)
    tk.Label(main_frame, text="Create an Event", font=("Arial", 20)).pack(pady=20)
    tk.Label(main_frame, text="Please remember your event ID, as you will need it for more.").pack(pady=5)

    entry_name = tk.Entry(main_frame)
    entry_name.pack(pady=10)
    entry_name.insert(0, "Enter the event name")
    entry_name.bind("<FocusIn>", onclick) 

    entry_type = tk.Entry(main_frame)
    entry_type.pack()
    entry_type.pack(pady=10)
    entry_type.insert(0, "Is the event individual or team-based?")
    entry_type.bind("<FocusIn>", onclick)

    entry_category = tk.Entry(main_frame)
    entry_category.pack()
    entry_category.pack(pady=10)
    entry_category.insert(0, "Is the event based on a sport or academic competition? (Sport/Academic)")
    entry_category.bind("<FocusIn>", onclick)

    result_laber = tk.Label(main_frame, text="")
    result_laber.pack(pady=5)

    def submit():
        eid=event_ID()
        

        events_list.append({
            'name': entry_name.get(),
            'type': entry_type.get(),
            'category': entry_category.get(),
            'ID': eid})
        save_data() #this will save the data to the JSON file after an event is added
        tk.Label(main_frame, text=f"Your event ID is: {eid}, you have successfully created the event!").pack(pady=5) 
        tk.Button(main_frame, text="Return to Home", command=show_home).pack(pady=5)
    
    submit_button = tk.Button(main_frame, text="Submit", command=submit)
    submit_button.pack(pady=5)

#Enter Results page
def enter_results_page():
    clear_frame(main_frame)
    tk.Label(main_frame, text="Enter Results", font=("Arial", 20)).pack(pady=20)
    tk.Label(main_frame, text="Please enter the event name, the name of the participant/team, and their final position (1-5).").pack(pady=5)
    
    enter_results_frame = tk.Frame(main_frame)
    enter_results_frame.pack(pady=10)
    entry_event = tk.Entry(enter_results_frame)
    entry_event.pack(pady=5)
    entry_event.insert(0, "Enter the event name")
    entry_event.bind("<FocusIn>", onclick)
    
    entry_participant = tk.Entry(enter_results_frame)
    entry_participant.pack(pady=5)
    entry_participant.insert(0, "Enter the name of the participant/team")
    entry_participant.bind("<FocusIn>", onclick)
    
    entry_position = tk.Entry(enter_results_frame)
    entry_position.pack(pady=5)
    entry_position.insert(0, "Enter the final position (1-5)")
    entry_position.bind("<FocusIn>", onclick)

    result_laber = tk.Label(main_frame, text="")
    result_laber.pack(pady=5)

    def submit():
        results_list.append({
            'event': entry_event.get(),
            'participant': entry_participant.get(),
            'position': int(entry_position.get()),
            'points': point_system.get(int(entry_position.get()), 0)}) #this will add the points to the results list based on the position of the participant/team, if the position is not between 1 and 5, it will default to 0 points
        save_data() 

        tk.Label(main_frame, text=f"Results for {entry_participant.get()} in {entry_event.get()} have been successfully entered!").pack(pady=5)
        tk.Label(main_frame, text=f"{entry_participant.get()} has been awarded {point_system.get(int(entry_position.get()), 0)} points for their position.").pack(pady=5)
        tk.Button(main_frame, text="Return to Home", command=show_home).pack(pady=5)
    submit_button = tk.Button(main_frame, text="Submit", command=submit)
    submit_button.pack(pady=5)




#Clear Function
def clear_frame(frame):
    for widget in frame.winfo_children():   
        widget.destroy()
#This will be used to clear the previous page when a new button is clicked by the user, for better structure and a more professional app


#------------------------------#
#Menu Buttons 

load_data() #this will load the data from the JSON file when the app is started, this ensures that the data is not lost when the app is closed 
show_home()  # home page start 

root.mainloop() 