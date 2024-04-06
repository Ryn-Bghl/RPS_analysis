import pandas as pd
from IPython.display import HTML

# DATA FORMATING

csvFile = open("stats.csv", "r")
data = csvFile.read()
data = data.split("\n")
val = []

for i in range(len(data)):
    data[i] = data[i].split(",")
    val.append(data[i])

data = val

# clean up the data
# remove the space in the values
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = data[i][j].replace(" ", "")


maxRound = len(data[0])/2
for i in range(len(data)):
    if maxRound < len(data[i])/2:
        maxRound = len(data[i])/2

maxRound = int(maxRound)

rounds = []
for i in range(maxRound):
    rounds.append("round " + str(i+1))

h_rock, h_paper, h_scissors, v_rock, v_paper, v_scissors = [], [], [], [], [], []
h_Rock, h_Paper, h_Scissors, v_Rock, v_Paper, v_Scissors = [], [], [], [], [], []

for i in range(maxRound):
    h_rock.append(0)
    h_paper.append(0)
    h_scissors.append(0)
    v_rock.append(0)
    v_paper.append(0)
    v_scissors.append(0)
    h_Rock.append(0)
    h_Paper.append(0)
    h_Scissors.append(0)
    v_Rock.append(0)
    v_Paper.append(0)
    v_Scissors.append(0)


for i in range(len(data)):
    for j in range(len(data[i])):
        if j % 2 == 0:
            if data[i][j] == "rock":
                h_rock[int(j/2)] += 1
            elif data[i][j] == "paper":
                h_paper[int(j/2)] += 1
            elif data[i][j] == "scissors":
                h_scissors[int(j/2)] += 1
        else:
            if data[i][j] == "rock":
                v_rock[int((j-1)/2)] += 1
            elif data[i][j] == "paper":
                v_paper[int((j-1)/2)] += 1
            elif data[i][j] == "scissors":
                v_scissors[int((j-1)/2)] += 1

for i in range(len(h_rock)):
    h_Rock[i] = round(h_rock[i]/(h_rock[i]+h_paper[i]+h_scissors[i]), 2)
    h_Paper[i] = round(h_paper[i]/(h_rock[i]+h_paper[i]+h_scissors[i]), 2)
    h_Scissors[i] = round(
        h_scissors[i]/(h_rock[i]+h_paper[i]+h_scissors[i]), 2)
    v_Rock[i] = round(v_rock[i]/(v_rock[i]+v_paper[i]+v_scissors[i]), 2)
    v_Paper[i] = round(v_paper[i]/(v_rock[i]+v_paper[i]+v_scissors[i]), 2)
    v_Scissors[i] = round(
        v_scissors[i]/(v_rock[i]+v_paper[i]+v_scissors[i]), 2)

h_rock, h_paper, h_scissors, v_rock, v_paper, v_scissors = h_Rock, h_Paper, h_Scissors, v_Rock, v_Paper, v_Scissors

H_rock = pd.Series(h_rock, index=rounds)
H_paper = pd.Series(h_paper, index=rounds)
H_scissors = pd.Series(h_scissors, index=rounds)
V_rock = pd.Series(v_rock, index=rounds)
V_paper = pd.Series(v_paper, index=rounds)
V_scissors = pd.Series(v_scissors, index=rounds)

df = pd.DataFrame(
    {'H_Rock': H_rock, 'H_Paper': H_paper, 'H_Scissors': H_scissors,
     'V_Rock': V_rock, 'V_Paper': V_paper, 'V_Scissors': V_scissors})
df.to_html('./Client/index.html')
df.to_json('./json/data.json')
