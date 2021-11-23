import csv
import statistics

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    sales = []

    for row in spreadsheet:
        monthly_sale = int(row['sales'])
        sales.append(monthly_sale)

total_sale = sum(sales)
average = statistics.mean(sales)
print(total_sale)

print("Average: ", average)

# i \in [0, 12-1) -> [0, 10]
for i in range(0, len(sales) - 1):
    print("{:2d}-{:2d}: {:.2f}%".format(i + 1, i + 2, (sales[i + 1] / sales[i] - 1) * 100))
    # print((i + 1), "-", (i + 2), ": ", sales[i + 1] / sales[i])

min_mon = -1
max_mon = -1
min_val = -1
max_val = -1
for i in range(0, len(sales) - 1):
    if (min_mon is -1) or (sales[i] < min_val):
        min_mon = i + 1
        min_val = sales[i]
    if (max_mon is -1) or (sales[i] > max_val):
        max_mon = i + 1
        max_val = sales[i]

print("Max Mon: ", max_mon)
print("Max Val: ", max_val)
print("Min Mon: ", min_mon)
print("Min Val: ", min_val)
