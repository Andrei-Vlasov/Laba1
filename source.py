f=open("pr_league1.csv", "r")
matches = [line.strip().split(',') for line in f]
teamCount = int(matches.pop(0)[0])
scores = []
for i in range(teamCount):
    for j in range(len(matches[i])):
        if ":" in matches[i][j]:
            matches[i][j] = matches[i][j].split(':')
            if matches[i][j][0] < matches[i][j][1]:
                matches[i][j] = 0
            elif matches[i][j][0] > matches[i][j][1]:
                matches[i][j] = 3
            elif matches[i][j][0] == matches[i][j][1]:
                matches[i][j] = 1
for i in range(teamCount):
    scores.append([matches[i].pop(0), sum(matches[i])])
for i in range(teamCount):
    scores[i][0], scores[i][1] = scores[i][1], scores[i][0]
scores.sort(reverse=True)
print(scores)