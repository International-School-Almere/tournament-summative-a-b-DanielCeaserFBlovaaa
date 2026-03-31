#main file for the Tournament App.
import random       #for user/team/event ID creation
import tkinter as tk

#File saving
import json         #for saving data in a JSON file

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
    
def add_team():
    name_team = input("Enter your team name: ")
    members_team = input("Enter the names of team members (comma separated): ")
    ID_team = print("Your team ID is: id(team)")

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