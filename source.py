from os.path import relpath
folder = relpath('resources')
file = 'pr_league1.csv'

def sort_by_score(file, folder):
    f = open(f"{folder}/{file}")
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
    return scores

def output_scoreboard(scores):
    with open("results.csv", "w") as result:
        for i in range(len(scores)):
            result.write(f"{scores[i][1]},{scores[i][0]}\n")


scores = sort_by_score(file, folder)
output_scoreboard(scores)
