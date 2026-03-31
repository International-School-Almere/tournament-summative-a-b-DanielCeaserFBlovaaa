#main file for the Tournament App.
import random       #for user/team/event ID creation
import tkinter as tk

#File saving
import json

#Global Variables:

"participants" = {} #stores individual participants and their details
"teams" = {}        #stores teams and their details
"events" = {}       #stores events and their details
"results" = {}      #stores results of events and the points awarded to participants/teams
"points_system" = {
    '1st': 10,
    '2nd': 8,
    '3rd': 5,
    '4th': 3,
    '5th': 1
}                 #point system used across the scoring system

#-------------------------------------------#
