import csv

candidates = []
votes = 0
results = dict()
precents = dict()

path = "election_data.csv"
with  open(path,newline ="") as csv_reader:
    data = csv.reader(csv_reader, delimiter=',')

    headers = next(data)

    for row in data:
        if row[2] in candidates:
            results[row[2]] += 1
        else:
            candidates.append(row[2])
            results.update({row[2]:1})

        votes += 1

for c in candidates:
    precents.update({c:results[c]/votes})

winner_percent = max(precents.values())
winner_name = [name for name in precents.items() if name == winner_percent]

print(dict(results))
print(candidates)
print(votes)
print(winner_percent)
print(winner_name)


