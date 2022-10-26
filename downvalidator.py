import pandas as pd
agmlist = []
nmelist = []
amtlist = []
cnclist = []
agmflist = []
acctslist = []
mdf = pd.read_csv("members.csv")
cdf = pd.read_csv("cancels.csv")
agmlist.extend(mdf.get("agreementnumber"))
nmelist.extend(mdf.get("membername"))
amtlist.extend(mdf.get("downpayment"))
cnclist.extend(cdf.get("membername"))
def activevalid(name1):
    if name not in cnclist:
        return True
def amtvalid(amount1):
    if amount1 < 100 and amount1 > 25:
        return True
i = 0
while i < len(nmelist):
    name = nmelist[i]
    amt = amtlist[i]
    agmt = agmlist[i]
    if activevalid(name) == True:
        if amtvalid(amt) == True:
            agmflist.append(agmt)
            acctslist.append(name)
    i += 1
    if i == len(nmelist):
        break
j = 0
print(acctslist)
