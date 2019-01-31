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
    

def greatest_profit (r):
        pv = profit_value
        pd = profit_date

        if int(r[1]) > pv:
                profit_value = int(r[1])
                profit_date = r[0]


def greatest_loss (r):
        pv = profit_value
        pd = profit_date       
    if int(r[1]) < loss_value:
        loss_value = int(r[1])
        loss_date = r[0]


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
    greatest_loss(first_row)
    greatest_profit(first_row)

    #Begin looping through the data
    for row in csv_data:
        months += 1
        net_profit += int(row[1])
        total_changes += int(row[1]) - last_profit
        last_profit = int(row[1])
        greatest_loss(row)
        greatest_profit(row)

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