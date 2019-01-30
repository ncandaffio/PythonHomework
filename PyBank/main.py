import csv

#Define path the csv file
path = 'budget_data.csv'

#Open the file and define new lines
with open(path,newline = '') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')

    # Define variables
    months = 0
    net_profit = 0
    total_changes = 0

    #Identify the header column
    headers = next(csv_data)

    #Manually calculate the first row as the average will not work without a datepoit to compare it to
    first_row = next(csv_data)
    months += 1
    net_profit += int(first_row[1])
    last_profit = int(first_row[1])

    #Begin looping through the data
    for row in csv_data:
        months += 1
        net_profit += int(row[1])
        total_changes += int(row[1]) - last_profit
        last_profit = int(row[1])

    #Calculate the average change
    average_change = total_changes / (months - 1)

    #Begin Printout
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total months: {months}")
    print(f"Net Profit: {'${:,.2f}'.format(net_profit)}")
    print(f"Average Change: {'${:,.2f}'.format(average_change)}")