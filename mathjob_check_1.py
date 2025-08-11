import feedparser
import tkinter as tk
from tkinter import ttk

#This short skript seaches for suitable jobs on Mathjobs and writes them into the csv file described in FILE_PATH

ACCEPTABLE_COUNTRIES = ["DE", "NL", "NO", "SE", "DK", "CH", "BE", "LU", "FR", "PL", "EE", "LV", "LT", "CZ", "HU", "GB", "FI"]
KEYWORDS_YES_NECESSARY = ["categor","Categor","homotop","Homotop","topolog","Topolog","mathematical physics","quantum","decarbonisation","decarbonization","greenhouse","climate","electricity","power"]
KEYWORDS_NO = ["PhD position","PhD Position","phd position"] #If these keywords are contained, disregard the listing
KEYWORDS_YES_OVERWRITE = ["postdoc","Postdoc"] # If these keywords are contained, take the listing, even if words from KEYWORDS_NO are contained
FILE_PATH = "/home/florian/Dokumente/python_projects/mathjob_check_files/job-search.csv"
KILL_MODE = False #In kill mode all previous listings are overwritten, generally I recommend to have it on "False"


if KILL_MODE:
    f = open(FILE_PATH, "w")
    f.close


#Gets the list of IDs already in the CSV document
list_ids_already_there = []
f = open(FILE_PATH, "r")
while True:
    line_read = f.readline()
    if line_read == "":
        break
    id_read = line_read.split(";")[0]
    list_ids_already_there.append(id_read)
f.close



#Gets the list of jobs filtered for the keywords I want
NewsFeed = feedparser.parse("https://www.mathjobs.org/jobs?joblist-0-0----rss--")
listofjobs=[]
for entry in NewsFeed.entries:
    description = entry.summary
    title = entry.title
    searchstring = title+" "+description
    yesorno=False
    if entry.id in list_ids_already_there:
        continue
    if not entry.ads_country in ACCEPTABLE_COUNTRIES:
        continue
    print(entry.title + ";" + entry.ads_univ +';' +  entry.ads_city+ ";" + entry.ads_state+   ";" + entry.ads_country+ ";" + entry.id)
    for keyword in KEYWORDS_YES_NECESSARY:
        if keyword in searchstring: yesorno=True
    if not yesorno: continue
    for keyword in KEYWORDS_NO:
        if keyword in searchstring: 
            #print("No No list word " + keyword + " was found in "+entry.id)
            yesorno=False
    for keyword in KEYWORDS_YES_OVERWRITE:
        if keyword in searchstring: 
            #print("YES YES list word " + keyword + " was found in "+entry.id)
            yesorno = True
    if yesorno:
        listofjobs.append(entry.id + ";" + entry.title + ";" + entry.ads_univ +';' +  entry.ads_city+ ";" + entry.ads_state+   ";" + entry.ads_country+ ";"
                            + entry.ads_deadline + ";" + entry.link[0:-4] + ";" + entry.title.replace("\n"," ").replace("\t"," ") +";" + entry.summary.replace("\n"," ").replace("\t"," ")+ ";" + entry.id)
print("New jobs found: " + str(len(listofjobs)))

#Writes the list of jobs into the CSV document
f = open(FILE_PATH, "a")
for line in listofjobs:
    f.write(line+ "\n")
f.close

root = tk.Tk()
root.title('Result')
root.geometry('400x200')
ttk.Label(root, text='Search had '+str(len(listofjobs)) +' results').pack()

root.mainloop()