import pandas as pd
agmlist = []
nmelist = []
datelist = []
amtlist = []
cnclist = []
agmflist = []
accdtlist = []
acctslist = []
pifdtlist = []
pifdf = pd.read_csv("cashpif.csv")
mdf = pd.read_csv("members.csv")
cdf = pd.read_csv("cancels.csv")
agmlist.extend(mdf.get("agreementnumber"))
nmelist.extend(mdf.get("membername"))
amtlist.extend(mdf.get("downpayment"))
datelist.extend(mdf.get("date"))
cnclist.extend(cdf.get("membername"))
pifdtlist.extend(pifdf.get("date"))
def activevalid(name1):
    if name not in cnclist:
        return True
def amtvalid(amount1):
    if amount1 < 100 and amount1 > 25:
        return True
def pifvalid(date1,pamt1):
    if date1 in pifdtlist:
        return True
i = 0
while i < len(nmelist):
    name = nmelist[i]
    amt = amtlist[i]
    agmt = agmlist[i]
    date = datelist[i]
    if activevalid(name) == True:
        if amtvalid(amt) == True:
            agmflist.append(agmt)
            acctslist.append(name)
            accdtlist.append(date)
        elif pifvalid(date) == True:
            agmflist.append(agmt)
            acctslist.append(name)
            accdtlist.append(date)
    i += 1
    if i == len(nmelist):
        break
for j in agmflist:
    print(acctslist+accdtlist)
