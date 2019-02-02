import csv

#Define objects
candidates = []
votes = 0
results = dict()
percents = dict()

#open and define csv
path = "election_data.csv"
with  open(path,newline ="") as csv_reader:
    data = csv.reader(csv_reader, delimiter=',')

#Define Headers
    headers = next(data)

#Loop through subsiquent data
    for row in data:

        #Check if candidate's name is in the dictionary
        if row[2] in candidates:
            #if so, add to the value
            results[row[2]] += 1
        else:
            #if not, add it with value 1
            candidates.append(row[2])
            results.update({row[2]:1})
        #Tally the vote
        votes += 1

#create a dictionary to hold the percentage
for c in candidates:
    percents.update({c:results[c]/votes})

#Find the winning percentage and name
winner_percent = max(percents.values())
winner_name = [name for name, number in percents.items() if number == winner_percent]

#Define function to print the dictionary to the terminal
def print_results(p):
    r = results
    for item in p:
        print(f"{item}: {'{:,.2f}%'.format(p[item]*100)} ({r[item]})")
        
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {votes}")
print("-----------------------------------")
print_results(percents)
print("-----------------------------------")
print(f"Winner: {winner_name[0]}")
print("-----------------------------------")

#Output to the text file
f = open("PyPoll_Results.txt","w")
f.write("Election Results\n")
f.write("-----------------------------------\n")
f.write(f"Total Votes: {votes}\n")
f.write("-----------------------------------\n")
for item in percents:
        f.write(f"{item}: {'{:,.2f}%'.format(percents[item]*100)} ({results[item]})\n")
f.write("-----------------------------------\n")
f.write(f"Winner: {winner_name[0]}\n")
f.write("-----------------------------------\n")
