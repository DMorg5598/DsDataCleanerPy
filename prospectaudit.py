## Prospect Cleaner and Analyzer
## import pandas and the data
import pandas as pd
prosdf1 = pd.read_csv("prospects.csv")
## drop duplicates by name
prosdf2 = prosdf1.drop_duplicates("name")
namelist = []
entdatlist = []
## declare lists with pre - specified origins and sources
originlist = ["web","ti","walk in","unsure"]
sourcelist = ["google","unsure","referral","previous member","drive by"]
totalprospects = len(namelist)
## add the names and entry dates to their respective lists
namelist.extend(prosdf2.get("name"))
entdatlist.extend(prosdf2.get("created date"))
## the invalidorigins function will determine if the origin is invalid
def invalidorigins(origin):
    if origin not in originlist:
        return True
## the invalidsources function will determine if the source is invalid
def invalidsources(source):
    if source not in sourcelist:
        return True
## loop through the list and fix the sources and origins
i = 0
while i < totalprospects:
    ogn = prosdf2.iat(i,"origin")
    src = prosdf2.iat(i,"source")
    if invalidorigins(ogn) == True:
        if ogn == "other":
            prosdf2.iat(i,"origin") = "unsure"
        elif ogn == "outreach":
            prosdf2.iat(i,"orgin") = "unsure"
    elif invalidsources(src) == True:
        if "other" in src:
            prosdf2.iat(i,"source") = "unsure"
        elif "website" in src:
            prosdf2.iat(i,"source") = "google"
        elif "online" in src:
            prosdf2.iat(i,"source") = "google"
    i += 1
    if i == totalprospects:
        break
## create lists to hold the count values
## loop through the list and count the sources and origins
while j < totalprospects:
    org = prosdf2.iat(j,"origin")
    src = prosdf2.iat(j,"source")
