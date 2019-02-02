import csv

candidates = []
votes = 0
results = dict()
percents = dict()


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
    percents.update({c:results[c]/votes})

winner_percent = max(percents.values())
winner_name = [name for name, number in percents.items() if number == winner_percent]

def print_results(p):
    r = results
    for item in p:
        print(f"{item}: {'{:,.2f}%'.format(p[item]*100)} ({r[item]})")

print(results)
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {votes}")
print("-----------------------------------")
print(print_results(percents))


