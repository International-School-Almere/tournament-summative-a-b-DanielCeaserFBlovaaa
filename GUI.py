import tkinter as tk
from turtle import onclick
root = tk.Tk() 
root.title("The Scoring System App")
root.geometry("1000x700") 
from main import add_participant, add_team, create_event, enter_results #This imports the fucntions from main.py to this file


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

show_main_frame() #this will show the main menu page when the app is opened

root.mainloop() 