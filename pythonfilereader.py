## ATTEMPT 1
## THIS FUNCTION WILL READ FOB SWIPES AND DETERMINE IF THEY ARE WITHIN THREE HOURS OF EACH OTHER
## the name function determines if the names match
def namefunction(member1,member2):
    if member1 in member2:
        return True
## the time function determines if the visits are within three hours of each other
def timefunction(visit1, visit2):
    if visit1 - visit2 < 180  or visit2 - visit1 < 180:
        return True
## take data and store it in a dataframe as "usagedataframe"
import pandas as pd
## create the name, visitid, and visitdate lists and variables
namelist = []
visitlist = []
visitidlist = []
doubleswipelist = []
doubleswipes = 0
dsmessage = "Total Doubleswipes:"
udf = pd.read_csv('usage.csv')
## group the list by name
newudf = udf.sort_values("membername")
## take the visitid column and store each # in a list a called "idlist"
visitidlist.extend(newudf.get("visitid"))
## take the column membername and store each name in a list called "namelist"
namelist.extend(newudf.get("membername"))
lastperson = namelist[0]
## take the visit column and store each time in a list called "visitlist"
visitlist.extend(newudf.get("visittime"))
lastvisit = visitlist[0]
## set the loop stop to the list length, then loop through the list
totalvisits = max(visitidlist)
i = 0
while i < len(visitidlist):
    name1 = namelist[i]
    name2 = lastperson
    time1 = visitlist[i]
    time2 = lastvisit
    i += 1
## if the names match, continue to the time function
    if namefunction(name1,name2) == True:
## if the times also match, count it as a double swipe
        if timefunction(time1,time2) == True:
            print("this is a doubleswipe")
            doubleswipes += 1
            lastvisit = time1
    lastperson = name1
print(dsmessage,doubleswipes)
