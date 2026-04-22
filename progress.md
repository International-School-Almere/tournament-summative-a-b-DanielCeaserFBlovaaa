# Progress Journal

> Use this journal to track progress, decisions, problems, and next steps.
> Update it after each work session.
> 
---

# 1. Project Overview

## Project Title
Tournament Scoring System Bram van Exel

## Project Description
In this project I will be designing, devoloping and testing a scoring system software for a tournament.

## Start Date
[30/03/2026]

## Target End Date
[18/04/2026]

## File list.

tournament_data.json


## (Dependencies) API / library / module list.
---


# 2. Progress Log

> Add a new session at the top each time you work.

---
## Session [01]
**Date:** [31/03/2026]  
**Time spent:** [45 Minutes]  
**Focus:**  
In this session I added import random, import tkinter and the global variables. I also added the funtions of adding participants, teams, events and results, as well as giving the participants, teams and events a random ID.
### Problems / Challenges
- Creating a good structure


### Solutions / Actions Taken
- Started explaining what certain things do, as well as seperating them in sections


### Evidence
- [Added code]


### Reflection
- What went well?
I was able to do this task fairly quickly without help. I was able to use my pseudocode and flowchart with the functions that had to be added, this allowed me to do it quickly and easily, and gave me time to already work on creating ID's for the tasks required. 
- What needs improvement?
My structuring skills in coding does need some improvement, as this will make it easier to go back to older code to change/improve it. However I did in the end improve it to make it more structured, which will help me in the long term.
- What did I learn?
I learned to seperate the sections and add comments/details to certain lines in the code to explain it and allow for future changes to be easier and more understandable for me.
---

## Session [02]
**Date:** [02/04/2026]  
**Time spent:** [1 Hour]  
**Focus:** [I have started on the JSON file handling, and have worked a lot on the GUI.]

### Problems / Challenges
- All pages were opening on start of program, only wanted the main menu to open.
- Buttons aren't working yet

### Solutions / Actions Taken
- I only used tk.Tk() for the main menu, when I used them for all all pages opened, now only one does. I also added show_main_frame() at the bottom to make sure thats the page that opens when app is started. 
- I have not yet fixed the button problem, however the "exit" button is working but this problem will be added to #7 below.

### Evidence
- [Added code]


### Reflection
- What went well?
I did a lot of problem solving on the start-up of the app, which allowed to fix a great amount of things not working and add a lot of things.
- What needs improvement?
My structure in coding, now everything is all over the place like functions at the bottom which would be better at the top, and more like that. As well as different files for different things which might make it harder.
- What did I learn?
I learned a lot of basic coding rules, for example that tk.Tk() can only be used for one of the pages, otherwise all the pages open at the start.

---
## Session [03]
**Date:** [03/04/2026]  
**Time spent:** [75 Minutes]  
**Focus:** [I fixed a lot with the GUI and mainly the buttons, however this is not finished yet but I have set myself up well to finish this in the next session. I also made some small changes/fixes, for example with the JSON file handling in which I was using dictionairies which makes it a little bit more challanging and is unnecesairy (for now).]

### Problems / Challenges
- Buttons of GIU and the programs structure
- 

### Solutions / Actions Taken
- I have (for now, maybe for always) put the GUI in main, this makes it a little more easy and organized for me, which will help me a lot
- 

### Evidence
- [Added code]


### Reflection
- What went well?
I was able to get a lot of work done and improve/add a lot of things, I am very happy with the improved structure of the entire project, with some parts being mentioned above like the GUI being put in the main file, but also small structural changes inside of the document.
- What needs improvement?
My work management does need some improvement, as I am taking a lot of time fixing things, instead of adding things. This could be due to the fact that I started too quick, and made a lot of mistakes which I now have to sit on the nails for. But this shouldn't be a major problem, as when this is fixed the app is practically done, with some things needed to be added. 
- What did I learn?
One specific thing I learned in this session was "side = left/right" for buttons or other GUI things like labels and etc. This allows the buttons to be lined up next to eachother, instead of stacked up on eachother which for me will look a lot better. I also decided to put the Exit button on the right side, for seperation and better visual appearanace. 


---
## Session [04]
**Date:** [06/04/2026]  
**Time spent:** [1 Hour]  
**Focus:** [I worked on the add participant/add team page in this session, my goal was to make both work + save data to JSON file. ]

### Problems / Challenges
- JSON File data saving
- Small mistakes made earlier in code

### Solutions / Actions Taken
- I did not quite do anything specific for the JSON file, it got solved when I was scanning through my code trying to find any mistakes I made, one example of this is mixing main_frame with root, which is also why some buttons did and didn't work, now that that is fixed and everything is main_frame all that is required to work does so.


### Evidence
- [Added code]


### Reflection
- What went well?
I was able to get a lot of work done, and finish my tasks that I had set for today, I was able to make the add participant and add team page and data saving work, and I am most proud of my issue scan that I did which allowed me to find and fix some issues that were making my code a lot less structured and some even caused the code to not work how I wanted it to.
- What needs improvement?
I will need to work on not making these small mistakes again, especially things like mixing root and main_frame which took very long for me to figure and solve. I will do this by writing these kinds of things down, like if I use a certain function for something, to remember this by writing it down so I can come back to it later.
- What did I learn?
I learned that issues in a code can be caused way further back, and that even if something works now, it might cause something else to malfunction later, so if I encounter another problem in the future I shouldn't just look in that section of the code, but also to older parts to find a fix.

---
## Session [05]
**Date:** [07/04/2026]  
**Time spent:** [1 Hour]  
**Focus:** [I worked on making the final pages work, so adding an event, and entering results. I also fixed a problem with my saving in JSON, as it only saved for one session and when I opened to app again then the old data would be removed. ]

### Problems / Challenges
- Data resets in JSON File


### Solutions / Actions Taken
- To fix this, I had to make some changes in my save_data function, as the JSON file would be opened as write, which means it will rewrite the data that is already in there and therefore remove it. I changed this to read, and added a load_data function which has now solved this problem and made the saving work.


### Evidence
- [Added code]


### Reflection
- What went well?
I was able to do a lot of work, and fix some older issues + make the app almost finished. I am most proud of my problem-solving skills used, where I was able to identify the saving problem and fix this using old code I made myself to try and identify a fix.

- What needs improvement?
I asked my teacher for some structural feedback, asking him about my structure of the code which he said was not optimal, as the most optimal layout is different than what I am doing right now. I will fix this later, as now I am trying to finish the code and worry about the structure later which might not be the smartest but works best for me.

- What did I learn?
I learned about the layout of an program, which will help me with my structure and keeping my code organized. 

---
## Session [06]
**Date:** [13/04/2026]  
**Time spent:** [75 Minutes]  
**Focus:** [In this session my main focus was making the leaderboard work, and adding drop-down menus when entering results to link it to a specific participant/team and event so it doesn't just duplicate in the leaderboard. ]

### Problems / Challenges
- Adding rank numbers to leaderboard (1. bram, 2. Testperson etc.)


### Solutions / Actions Taken
- To solve this, I added "enumerate" with the required code to it, this now allows me to have the rankings be in order of highest points first, with the fitting number to it.


### Evidence
- [Added code]


### Reflection
- What went well?
I was able to finish the leaderboard and now will start finalizing the code, and adding the final details to it. This went pretty well as I planned it would take multiple sessions to get it fully up and running but took a lot shorter than expected. The drop-down menu feature was also a lot easier than expected, it kind of just worked immidiatly without too much hassle except for finding the correct names for some of the things.

- What needs improvement?
I need to make sure the participants and teams are seperated on the leaderboard, not quite sure yet how I will do this but that is for the next session. Doing this will make the app even more user-friendly + now teams/participants will not be able to see their real rank among their group (either other participants or other teams)

- What did I learn?
My main learning point for this session was definetly learning about "enumerate" which helps my program a lot and will be used for different programs in the future as well.

---
## Session [07]
**Date:** [15/04/2026]  
**Time spent:** [30 Minutes]  
**Focus:** [Adding a maximum amount of allowed participants/teams and test plan improvement; adding "return to home" button on each page, without requiring the user to submit work.]

### Problems / Challenges
- One challenge was to find the easiest and most organized way of adding the button for myself (the developer)


### Solutions / Actions Taken
- I created a new function: add_home_button() in which I put the code, then I was able to just add that function in all the other page functions (add_participant(), add_team(), etc.) which was very easy and structured for me to do.


### Evidence
- [Added code]


### Reflection
- What went well?
I was able to find the method of adding the button, in the easiest and most structured way fairly quickly, as well as that it worked on first try and didn't require any other changes to the code to be made. In this session I was also able to add a maximum number of participants and teams in the program, which further improves the user experience and the ease-of-use. This went fairly easy as I just looked at past code in which I had to do a similar thing, and used that code in this program as well. 

- What needs improvement?
From this session I don't believe anything specificly needs improvement.

- What did I learn?
Adding the function in each page function allowed me to fix and improve my code very quick, which is definetly a learning point for adding global buttons like that. 

---
## Session [08]
**Date:** [16/04/2026]  
**Time spent:** [2 Hours]  
**Focus:** [In this session main focus was to seperate the leaderboard into a team leaderboard and participant leaderboard, which was one of the main problems my program was having]

### Problems / Challenges
- I tried creating seperate pages for participants and teams to have their own leaderboard, however this didn't quite go as planned and got me stuck in a loop of issues and eventually got to the point that for me it became unreadable and looked unfixable


### Solutions / Actions Taken
- I went back to the 10th Commit, took the code from there and restored the program back to that version. This does mean I am a little less far than I planned on being but it's better than the state I was in with the leaderboard.


### Evidence
- No evidence required


### Reflection
- What went well?
All was restored to old version

- What needs improvement?


- What did I learn?


---
## Session [09]
**Date:** [17/04/2026]  
**Time spent:** [45 Minutes]  
**Focus:** [In this session main focus was to seperate the leaderboard into a team leaderboard and participant leaderboard, which was one of the main problems my program was having and continued on from the session yesterday. I also managed to stop duplicate particiapant and teams to be added. ]

### Problems / Challenges
- It was a challenge to figure out how to make sure they are not mixed in one leaderboard, but slowly and steadily figured out how to do it throughout this session.


### Solutions / Actions Taken
- I looked at ways in which I could check if the name is either in a participant or teams list, which I then found out how to do it from old code I wrote from which I got the code that helped me a lot. For the duplicate checking, it was also taken from an old code, which I was able to use very quickly.

### Evidence
- [Added code]


### Reflection
- What went well?
I am very happy with my ability of not giving up on this leaderboard problem, and restarting from before my session tomorrow to make sure I stay organized and understand the code. Today, I was able to find a fix for both focuses in this session from old code, which made it a lot quicker and easier to fix it. 

- What needs improvement?
This all stammed from old laziness/issues in my code from where I didn't initially "finish" the full function, which came back to me now and I had to go back to that part of the code and find fixes, which would be easier to do in the session that I created the leaderboard.

- What did I learn?
In the future, I will rely more on my old codes to find fixes instead of having to go over my code myself. This will save me a lot of time and effort and make it a lot easier to fix problems or find new features that I can add into a program.

---
## Session [10]
**Date:** [21/04/2026]  
**Time spent:** [45 Minutes]  
**Focus:** [In this session I collected peer feedback, and from there improved 2 of the points that were given to me. 1: Fixing the fact that users can submit empty boxes in some features, and 2: Fixing that users are able to write in the drop-down menus.]

### Problems / Challenges
- There wasn't an significant challenge in this session, everything ran quite smoothly and fixes were found fairly quickly and easily. 


### Solutions / Actions Taken
- In this session I collected peer feedback, which has given me another perspective on my program and allows me to improve it even further. Both focuses in this session were found quick, with simple changes requiring minimal changes in my code. This allows me to keep the structure I want in my code, and allows for easier maintanance and problem-solving for now, and in the future. 

### Evidence
- [Added code]


### Reflection
- What went well?
Finding the fixes that were recommended by the peer feedback was very simple and quick, allowing me to spend more time on my reflection and making sure the new fixes fully work without any issues, which will help me in the future as I won't have to go back to fix it (doing the opposite of this and not testing the new fixes was mentioned in past progress sessions as well, where I mentioned I need to work on this so I have improved majorly on this.)

- What needs improvement?
In future sessions I will work on the other feedback points which needs to be fixed.

- What did I learn?
I learned a lot about making sure that the fix is actually fixed now, instead of a half-fix and then moving on to the next thing to be quicker. This in the end allows me to save more time and energy, and create a more professional program and structure.
---
## Session [11]
**Date:** [22/04/2026]  
**Time spent:** [30 Minutes]  
**Focus:** [In this session, the main focus was removing the OnClick function which wasn't working before, and putting the text inside the boxes outside, to get rid of the problem of the users having to remove the text inside boxes themselves.]

### Problems / Challenges
- It was a "lightbulb" moment for me, to just get rid of OnClick, and putting the text outside the boxes to get rid of the problem. Finding this was a long trial of trying stuff and things not working. But it has paid off.


### Solutions / Actions Taken
- I had decided to re-design the boxes, and now have just put the description texts above the boxes instead of inside of them. This only took removing some lines of code and changing small parts of them (for exammple: removing the lines containing "OnClick" and "Insert" which has now given me the fix.)

### Evidence
- [Added code]


### Reflection
- What went well?
I have further progressed with the code and am now finalizing it, which allows me to focus on the reflection and finding any more bugs that I could've looked over. This shows good time and work management, which is helping me a lot right now.

- What needs improvement?
I have one more point of teacher feedback, which is to make a seperate page to view the participants/teams and events data.

- What did I learn?
I have learned that sometimes, the best fix is just to change the design, which I had done to find the OnClick fix. 

# 7. Problems and Fixes

| Problem | Cause | Fix | Status |
|---|---|---|---|

| All buttons except for the exit button do not work | The most likely cause of this problem was that main_frame was being mixed with root, this caused for some buttons to be paired to main_frame which was used for the GUI, but also some to root which caused those not to work. | I put everything under main_frame, which was a simple but confusing fix, and required me to scan through my entire code and find all that are linked to root. | FIXED|


---

# 11. Final Reflection

> Complete this section at the end of the project.

## What I achieved
- 
- 
- 

## What worked well
- 
- 
- 

## What did not work well
- 
- 
- 

## What I would improve next time
- 
- 
- 

## Final outcome
[Describe the final result]

## Did I meet the success criteria (designspecifications)?
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Final evaluation
[Write a short final judgment of the project]

---
- 
