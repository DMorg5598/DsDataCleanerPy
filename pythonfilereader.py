## ATTEMPT 1
visits = []
visit1 = 0
visit2 = 0
strikes = 0
totalvisits = 0
name1 = 0
name2 = 0
time1 = 0
time2 = 0
x = 1
## ReadCycle Function
f = open("usage.txt", "r")
while x in f:
    visits.append(f.readline())
    totalvisits += 1
    continue
## NameMatcher Function
def namechecker(name1,name2)
    if name1 == name2:
        continue
myfunction()
## TimeMatcher Function
        time1 = visit1[18:35]
        time2 = visit2[18:35]
        if time1 == time2:
            stikes += 1
    else:
        continue
print(strikes)
print("Total visit = ")
print(totalvisits)

## ATTEMPT 2
import pandas as pd
namelist = []
vdf = []
doublevisits = 0
udf = pd.read_csv('usage.csv')
namelist.extend(udf.get("membername"))
for i in range(len(namelist)):
  j = i + 1
  name1 = namelist[i]
  name2 = namelist[j]
  if name1 == name2:
   print("These names match")
   doublevisits += 1
print("Double Visits:")
print(doublevisits)
