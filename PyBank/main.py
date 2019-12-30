# setting path for csv file
csvpath = Path('../../../CU-NYC-FIN-PT-12-2019-U-C/Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv')

# creating variables
month_count = 0
total_pnl = 0
pnl_list = []
date_list = []
profit_increase = ''
profit_decrease = ''

# opening csv file to be read
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # skipping header
    csv_header = next(csvreader)
    
    # iterating over rows in the csv file and setting varibles for column lists
    for row in csvreader:
        date = row[0]
        pnl = row[1]
        
        # counting number of rows in the csv file and assigning this value to variable
        month_count += 1
        
        #summing pnl values
        total_pnl += int(pnl)
        
        # creating list of pnl values
        pnl_list.append(int(pnl))
        
        #creating a list of dates
        date_list.append(date)
    
    # creating variables for change values and a list to store these values
    pnl_change = 0
    pnl_change_list = []
    
    # setting first value of change value list to zero
    pnl_change_list.append(0)
    
    # iterating through the list of adjacent pnl values
    for value_1, value_2 in zip(pnl_list[::1], pnl_list[1::1]):

        # calculate the change and store this value in a variable
        pnl_change = value_2 - value_1
            
        # and add this variable to the change value list
        pnl_change_list.append(pnl_change)
      
    # sum changes for average
    sum_of_changes = 0
    
    for value in pnl_change_list:
        sum_of_changes += int(value)
    
    # calculating average change
    average_change = float(sum_of_changes) / len(pnl_change_list)
    
    # creating a dictionary to associate the list of dates and list of pnl changes
    dates_and_pnl = {date_list[i] : pnl_change_list[i] for i in range(len(date_list))}
    
    # setting variables to track largest profits and losses
    max_profit = 0
    max_loss = 0
    
    # iterating through the dictionary and return the largest profits and losses
    for date, value in dates_and_pnl.items():
        if value > max_profit:
            max_profit = value
        if value < max_loss:
            max_loss = value
            
    # printing out summary statistics
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${total_pnl}')
    print(f'Average  Change: ${average_change}')
    for date, value in dates_and_pnl.items():
        if value == max_profit:
            print(f'Greatest Increase in Profits: {date} | ${value}')
        if value == max_loss:
            print(f'Greatest Decrease in Profits: {date} | ${value}')