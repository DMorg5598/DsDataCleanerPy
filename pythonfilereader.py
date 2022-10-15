## ATTEMPT 1
## take data and store it in a dataframe as "usagedataframe"
import pandas as pd
namelist = []
visitlist = []
visitidlist = []
doubleswipelist = []
doubleswipes = 0
udf = pd.read_csv('usage.csv')
newudf = udf.sort_values(by = 'membername')
## sort the list
## take the visitid column and store each # in a list a called "idlist"
visitidlist.extend(newudf.get("visitid"))
## take the column membername and store each name in a list called "namelist"
namelist.extend(newudf.get("membername"))
## take the visit column and store each time in a list called "visitlist"
visitlist.extend(newudf.get("visittime"))
## the name function determines if the names match
def namefunction(name1):
    if name1 == name2:
        lastperson = name2
        return
        True
## the time function determines if the visits are within three hours of each other
def timefunction(visit1, visit2):
    if visit1 - visit2 < 180  or visit2 - visit1 < 180:
        return
        True
## loop through the list and pass the names through the namefunction
i = 0
while i < len(namelist):
    i = i + 1
    name1 = namelist[i]
    namefunction(name1,name2)
    if namefunction(name1,name2) == True:
        visit1 = visitlist[i]
        visit2 = visitlist[j]
        if visitfunction(visit1,visit2) == True:
            doubleswipelist.extend(x)
            doubleswipes += 1
    if i == 12:
        break
print("these visit id numbers")
print(doubleswipelist)
print("are double swipes")
print(doubleswipes)
