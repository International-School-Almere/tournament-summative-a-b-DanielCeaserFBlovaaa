import tkinter as tk

from main import add_participant, add_team, create_event, enter_results #This imports the fucntions from main.py to this file

#-----------------------------#
#Main Menu page
root=tk.Tk()
root.title("The Scoring System App")
root.geometry("1000x700")

#Add Participant page
root_participant=tk.Tk()
root_participant.title("Add a Participant")
root_participant.geometry("1000x700")

#Add Team page
root_team=tk.Tk()
root_team.title("Add a Team")
root_team.geometry("1000x700")

#Create Event page
root_event=tk.Tk()
root_event.title("Create an Event")
root_event.geometry("1000x700")

#Enter Results page
root_results=tk.Tk()
root_results.title("Enter Results")
root_results.geometry("1000x700")


# Here is where I will be creating the buttons for the main menu
addparticipant_button = tk.Button(root, text="Add a participant")
addparticipant_button.pack(pady=10)


addteam_button = tk.Button(root, text="Add a team")
addteam_button.pack(pady=10)


createevent_button = tk.Button(root, text="Create an event")
createevent_button.pack(pady=10) 


enterresults_button = tk.Button(root, text="Enter results")
enterresults_button.pack(pady=10)


exit_button = tk.Button(root, text="Exit", command=root.quit) #command=root.quit will close the app when exit button is clicked
exit_button.pack(pady=10)

#pack(pady=10) is used to display the buttons, where "pady" spaces them out to add structure and better visuals

#------------------------------#
#linking buttons to functions from main.py using if/elif/else


if addparticipant_button:
    root_participant.mainloop() #this will open the add participant page when the button is clicked
elif addteam_button:
    root_team.mainloop() #this will open the add team page when the button is clicked
elif createevent_button:            
    root_event.mainloop() #this will open the create event page when the button is clicked
elif enterresults_button:
    root_results.mainloop() #this will open the enter results page when the button is clicked
elif exit_button:
    root.quit()
         



root.mainloop()