import csv

#Define path the csv file
path = 'budget_data.csv'


# Define variables
months = 0
net_profit = 0
total_changes = 0
loss_value = 0
profit_value = 0
profit_date = "none"
loss_date = "none"
    

#Open the file and define new lines
with open(path,newline = '') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')

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
        profit_change = int(row[1]) - last_profit
        if profit_change > profit_value:
                profit_value = profit_change
                profit_date = row[0]
        if profit_change < loss_value:
                loss_value = profit_change
                loss_date = row[0]
        total_changes += profit_change
        last_profit = int(row[1])

    #Calculate the average change
    average_change = total_changes / (months - 1)


    #Begin Printout
    print("Financial Analysis")
    print("-------------------------------")
    print(f"Total months: {months}")
    print(f"Net Profit: {'${:,.2f}'.format(net_profit)}")
    print(f"Average Change: {'${:,.2f}'.format(average_change)}")
    print(f"Greatest Increase in Profits: {profit_date} {'${:,.2f}'.format(profit_value)}")
    print(f"Greatest Decrease in Profits: {loss_date} {'${:,.2f}'.format(loss_value)}") 

    #Text File output
    f = open("PyBank_Financial_Analysis.txt","w")
    f.write("Financial Analysis\n")
    f.write("-------------------------------\n")
    f.write(f"Total months: {months}\n")
    f.write(f"Net Profit: {'${:,.2f}'.format(net_profit)}\n")
    f.write(f"Average Change: {'${:,.2f}'.format(average_change)}\n")
    f.write(f"Greatest Increase in Profits: {profit_date} {'${:,.2f}'.format(profit_value)}\n")
    f.write(f"Greatest Decrease in Profits: {loss_date} {'${:,.2f}'.format(loss_value)}\n") 