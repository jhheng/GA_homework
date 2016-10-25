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
    file_nested_list = [row for row in reader]

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
average_price = round(total_price/no_unique_order_id,2)

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
soft_drinks =[]
for row in data:
    if row[2] == "Canned Soda" or row[2] == "Canned Soft Drink":
        soft_drinks.append(row[3])

unquie_soft_drinks = set(soft_drinks)

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

burrito_toppings = []
no_burrito = []
for row in data:
    if "Burrito" in row[2]:
        burrito_toppings.append(row[3])
        no_burrito.append(int(row[1]))
total_burrito = sum(no_burrito)
total_toppings=0
for top in burrito_toppings:
    total_toppings += len(top.split(','))

average_topping_per_burrito = round((1.00 * total_toppings)/total_burrito,2)

'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
from collections import defaultdict

counter = defaultdict(int)
chips=[]
total_chips_order = []
for row in data:
    if "Chips" in row[2]:
        chips.append(row[2])
        total_chips_order.append(int(row[1]))
# CHECK ON SAT WHY IS THIS WRONG??
#for i in range(len(chips)):
    #counter[chip[i]] += total_chips_order[i]
    #print counter


'''
Question that interest me: What is the item that generates the most revenue?
Assume item price is for 1 quantity. take quantity into account.
'''

#all_items_names =[]
#all_items_names = [data[i][2] for i in range(len(data))]
import operator
revenue = defaultdict(float)
for row in data:
    revenue[row[2]] += round(float(row[-1].strip('$')),2) * round(float(row[1]),2)

sorted_rev = sorted(revenue.items(), key=operator.itemgetter(1))
print sorted_rev[-1]
