'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

file_nested_list =[]
with open('orders.tsv') as f:
    reader = csv.reader(f,delimiter = '\t')
    for row in reader:
        file_nested_list.append(row)

print file_nested_list

'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''

header = file_nested_list[0]
data = file_nested_list[1:]

'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
order_id = [row[0] for row in data]
no_unique_order_id = len(set(order_id))
prices = [float((row[-1].strip('$')).strip()) for row in data]
total_price  = sum(prices)
average_price = total_price/no_unique_order_id
