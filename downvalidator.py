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
pifamtlist = []
pifdf = pd.read_csv("transactions.csv")
mdf = pd.read_csv("members.csv")
cdf = pd.read_csv("cancels.csv")
agmlist.extend(mdf.get("agreementnumber"))
nmelist.extend(mdf.get("membername"))
amtlist.extend(mdf.get("downpayment"))
datelist.extend(mdf.get("date"))
cnclist.extend(cdf.get("membername"))
pifdtlist.extend(pifdf.get("date"))
pifamtlist.extend(pifdf.get("amount"))
def activevalid(name1):
    if name not in cnclist:
        return True
def amtvalid(amount1):
    if amount1 < 100 and amount1 > 25:
        return True
def pifvalid(date1,pamt1):
    if date1 not in pifdtlist and pamt1 > 380:
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
        elif pifvalid(date,amt) == True:
            agmflist.append(agmt)
            acctslist.append(name)
            accdtlist.append(date)
    i += 1
    if i == len(nmelist):
        break
j = 0
while j < len(agmflist):
    print(agmflist[j],acctslist[j],datelist[j])
    j += 1
