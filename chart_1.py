import pandas as pd
import matplotlib.pyplot as plt

# step 1 read data :
file = "Messi.csv"
df = pd.read_csv(file)
# print(df)

# step 2 display your data
sample = df.head(10)
# print(sample)

# step 3 stat :
stat = df.describe()
# print(stat)

# step 4 acces colum

pos_team_1 = df["possession team1"]
pos_team_2=df["possession team2"]
goal_team_1=df["number of goals team1"]
goal_team_2=df["number of goals team2"]

# figure A
plt.figure("World Cup")
plt.subplot(121)
plt.title ( " Team 1 ")
plt.scatter ( goal_team_1 , pos_team_1)
plt.xlabel (" Team 1 Goals")
plt.ylabel (" Team 1 Posestion")
plt.subplot(122)
plt.title ( " Team 2 ")
plt.bar ( goal_team_2 , pos_team_2)
plt.xlabel (" Team 2 Goals")
plt.ylabel (" Team 2 Posestion")
plt.show()

# print(df[["number of goals team1","number of goals team2"]])