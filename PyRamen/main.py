## Part 1: Read the Data

# importing libraries
from pathlib import Path
import csv

# setting path for csv file
menu_csvpath = Path('../../../CU-NYC-FIN-PT-12-2019-U-C/Homework/02-Python/Instructions/PyRamen/Resources/menu_data.csv')

# initializing menu list
menu = []

# opening csv file to be read
with open(menu_csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # skipping header
    csv_header = next(csvreader)
    
    # initializing lists for each column in the csv file
    item_list = []
    category_list =[]
    description_list = []
    price_list = []
    cost_list = []
    
    # iterating over rows in the csv file
    for row in csvreader:
        
        # setting varibles for items in each row
        item = row[0]
        category = row[1]
        description = row[2]
        price = float(row[3])
        cost = float(row[4])

        # appending the items in each column to a corresponding list
        item_list.append(item)
        category_list.append(category)
        description_list.append(description)
        price_list.append(price)
        cost_list.append(cost)
        
    # appending lists to create menu list of lists
    menu.append(item_list)
    menu.append(category_list)
    menu.append(description_list)
    menu.append(price_list)
    menu.append(cost_list)

# setting path for csv file
sales_csvpath = Path('../../../CU-NYC-FIN-PT-12-2019-U-C/Homework/02-Python/Instructions/PyRamen/Resources/sales_data.csv')

# initializing sales list
sales_list = []

# opening csv file to be read
with open(sales_csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # skipping header
    csv_header = next(csvreader)
    
    # initializing lists for each column in the csv file
    line_item_list =[]
    date_list =[]
    card_number_list =[]
    quantity_list = []
    sales_item_list = []
    
    # iterating over rows in the csv file
    for row in csvreader:
        
        # setting varibles for items in each row
        line_item = row[0]
        date = row[1]
        card_number = row[2]
        quantity = int(row[3])
        sales_item = row[4]
        
        # appending the items in each column to a corresponding list
        line_item_list.append(line_item)
        date_list.append(date)
        card_number_list.append(card_number)
        quantity_list.append(quantity)
        sales_item_list.append(sales_item)
    
    # appending lists to create sales list of lists
    sales_list.append(line_item_list)
    sales_list.append(date_list)
    sales_list.append(card_number_list)
    sales_list.append(quantity_list)
    sales_list.append(sales_item_list)

## Part 2: Manipulate the Data

# creating empty dictionary to store results 

report = {}

# iterating through list of sales items and adding unique sales items to the report dictionary 
# with metrics

for sales_item in sales_item_list:
    if sales_item not in report:
        report[sales_item] = {
            '01-count' : 0,
            '02-revenue' : 0,
            '03-cogs' : 0,
            '04-profit' : 0
        }

# iterating over menu items and related stats, and over sales items and related stats to determine
# metrics for each menu item in the report dictionary
        
for item, price, cost in zip(item_list, price_list, cost_list):
    for sales_item, quantity in zip(sales_item_list, quantity_list):
        if item == sales_item:
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += (price - cost) * quantity

# setting output file name
output = 'report_metrics.txt'

# opening the output path as a file object and writing to file
with open(output, 'w') as file:
    file.write(str(report))