# Filename: P10_Arrays2D_azha4978.py
# Author: Alan Zhao
# Date: 02/05/16
# Purpose: Create a 2D array to meet certain requirements.
# All empty print statements are for whitespace and readability unless otherwise specified.

# 2D Arrays
product_array = []
sales_order_array = []

# 1D Arrays to be appended into 2D Arrays
name_list = []
cost_list = []
quantity_list = []
price_list = []
order_list = []
total_sales_order_list = []
total_sales_order_list1 = []

# Populate the 2D array
# Store product names
for a in range(0, 5):     
    name = input("Enter products one by one: ")
    name_list.append(name)
product_array.append(name_list)
print()

# Store costs of each product
for b in range(0, 5):
    cost = float(input("Enter the cost of %s in US dollars: " % name_list[b]))
    cost_list.append(cost)
product_array.append(cost_list)
print()

# Store quantity of each product
for c in range(0, 5):
    quantity = float(input("Enter the quantity of %s in US dollars: " % name_list[c]))
    quantity_list.append(quantity)
product_array.append(quantity_list)
print()

# Print table of information
print("Product Name: %s, Cost: $%4.2f, Quantity: %.0f" %(product_array[0][0], product_array[1][0],
                                                         product_array[2][0]))
print()
print("Product Name: %s, Cost: $%4.2f, Quantity: %.0f" %(product_array[0][1], product_array[1][1],
                                                         product_array[2][1]))
print()
print("Product Name: %s, Cost: $%4.2f, Quantity: %.0f" %(product_array[0][2], product_array[1][2],
                                                         product_array[2][2]))
print()
print("Product Name: %s, Cost: $%4.2f, Quantity: %.0f" %(product_array[0][3], product_array[1][3],
                                                         product_array[2][3]))
print()
print("Product Name: %s, Cost: $%4.2f, Quantity: %.0f" %(product_array[0][4], product_array[1][4],
                                                         product_array[2][4]))
print()

# Input markup
for d in range(0, 5):
    markup = float(input("Enter the percentage markup of %s: " % product_array[0][d]))
    price_list.append((100 + markup) * product_array[1][d] / 100)
product_array.append(price_list)
print("The markup percentage and price have been stored.")
print()

# Print new table of information
print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f" %(product_array[0][0], product_array[1][0],
                                                                        product_array[3][0], product_array[2][0]))
print()
print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f" %(product_array[0][1], product_array[1][1],
                                                                        product_array[3][1], product_array[2][1]))
print()
print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f" %(product_array[0][2], product_array[1][2],
                                                                        product_array[3][2], product_array[2][2]))
print()
print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f" %(product_array[0][3], product_array[1][3],
                                                                        product_array[3][3], product_array[2][3]))
print()
print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f" %(product_array[0][4], product_array[1][4],
                                                                        product_array[3][4], product_array[2][4]))
print()

# Input information into sales order another 2D array
for e in range(0, 5):
    order = int(input("How many of %s were ordered? " % product_array[0][e]))
    order_list.append(order)
sales_order_array.append(order_list)
print()

for f in range(0, 5):
    total_sales_order_list.append(sales_order_array[0][f] * product_array[3][f])
sales_order_array.append(total_sales_order_list)

total_sales_order = 0      # Accumulator variable
for g in range(0, 5):
    total_sales_order += sales_order_array[0][g] * product_array[3][g]
total_sales_order_list1.append(total_sales_order)

# Print final table of information
print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f, Sales Order: $%4.2f" %(product_array[0][0],
product_array[1][0], product_array[3][0], product_array[2][0], sales_order_array[1][0]))
print()

print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f, Sales Order: $%4.2f" %(product_array[0][1],
product_array[1][1], product_array[3][1], product_array[2][1], sales_order_array[1][1]))
print()

print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f, Sales Order: $%4.2f" %(product_array[0][0],
product_array[1][2], product_array[3][2], product_array[2][2], sales_order_array[1][2]))
print()

print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f, Sales Order: $%4.2f" %(product_array[0][0],
product_array[1][3], product_array[3][3], product_array[2][3], sales_order_array[1][3]))
print()

print("Product Name: %s, Cost: $%4.2f, Price: $%4.2f, Quantity: %.0f, Sales Order: $%4.2f" %(product_array[0][0],
product_array[1][4], product_array[3][4], product_array[2][4], sales_order_array[1][4]))
print()
print("Total sales order of all items combined: $%4.2f", % total_sales_order_list1[0])






