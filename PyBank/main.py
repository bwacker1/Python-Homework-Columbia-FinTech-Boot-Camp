# import libraries
from pathlib import Path
import csv

# setting path for csv file
csvpath = Path('../../../CU-NYC-FIN-PT-12-2019-U-C/Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv')

# creating variables
month_count = 0
total_pnl = 0
pnl_list = []
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
    
    # creating variables for change values and a list to store these values
    pnl_change = 0
    pnl_change_list = []
    
    # creating variables to reference where we are in the list - these will be increased as we iterate
    # through the list of pnl values to change the inputs to the change value calculation
    ref_value_1 = 0
    ref_value_2 = 1
    
    # settings variables for change value calculation
    value_1 = pnl_list[ref_value_1]
    value_2 = pnl_list[ref_value_2]
    
    # setting first value of change value list to the first value in the list - i.e. difference between
    # first value and zero
    pnl_change_list.append(value_1)
    
    # iterating through the list of pnl values
    for value in pnl_list:
            
        # increase the list index number we are referencing in the list by 1
        ref_value_1 += 1
        ref_value_2 += 1
            
        # and assign the corresponding values to the change value calculation inputs
        # value_1 = pnl_list[ref_value_1]
        value_2 = pnl_list[ref_value_2]
            
        # then calculate the change and store this value in a variable
        pnl_change = value_2 - value_1
            
        # and add this variable to the change value list
        pnl_change_list.append(pnl_change)