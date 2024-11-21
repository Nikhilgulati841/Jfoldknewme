import pandas as pd

data_dict={"T-Slots":["@4:10 Am","@4:30 Am","@10:00 Am","@11:00 Am","@12:00 Pm",
"@5:00 Pm","@5:40 Pm","@6:00 Pm","@6:20 Pm","@7:45 Pm","@10:45 Pm","@1:30 Am","@3:45 Am"],

"DEFINED TASKS          ":["Reached Room","Start Studying","Study till here","Revision Time",
                        "Exercise|bath|1st Meal|Sleep","Sleep Till here","Ready for Office",
                        "Office Ride Book","Office On Time","Eat Protien full food",
                        "2nd Meal | FDD Filling","Next day Plan","Ride #back to Room"],
                        
        "REMINDER   ":["NO Distraction","FreshUp|10m BrB","","Mandate",5,6,7,8,9,10,11,12,13],
        "Need HELP..!!":["No Talking|Smoking","20-Water-Face-Splash",3,"Mandate",5,6,7,8,9,10,11,12,13]}

data=pd.DataFrame(data_dict) #Other approach--> data=pd.DataFrame(data_dict,column="T-Slots","DEFINED TASKS          ",
#""... etc like that )
# data["TASKS"].str.pad(width=4,fillchar="T",side="both")
data=data.set_index("T-Slots")

print("""\nFor the spare time, If you do the task in less time.
Remember Not to rest | As the TIME LEFT is the TIME you GAINED.
So, Either do the Next Task or Increase your Productivity.
Take Break | Meditate | Pull-ups | Push-ups""")
print("===================================================\n")

print(data)
print("===================================================\n")

#hello
#changes from local to remote 