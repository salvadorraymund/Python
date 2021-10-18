import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)
    line_count = 0
    for row in csv_reader:
        print(row)
    #     if line_count == 0:
    #         print(f'Column names are {", ".join(row)}')
    #         line_count += 1
    #     else:
    #         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')


# with open('employee_birthday.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         print(row)
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["name"]} works in the {row["departments"]} department, and was born in {row["birthday month"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')

# with open('employee_address.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {",".join(row)}')
#             line_count += 1
#         else:
#             print(f'{row[0]} lives at {row[1]} and has been with the company since {row[2]}')
#             line_count += 1
#     print(f'Processed {line_count} lines.')

header = ['id', 'name', 'address', 'zip']
rows = [
    [1, 'Hannah', '4891 Blackwell Street, Anchorage, Alaska', 99503],
    [2, 'Walton', '4223 Half and Half Drive, Lemoore, California', 97401],
    [3, 'Sam', '3952 Little Street, Akron, Ohio', 93704],
    [4, 'Chris', '3192 Flinderation Road, Arlington Heights, Illinois', 62677],
    [5, 'Doug', '3236 Walkers Ridge Way, Burr Ridge', 61257],
]

with open('customers.cv', 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    for row in rows:
        csv_writer.writerow(row)

with open('customers.cv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

with open('customers.cv', 'r') as a_reader, open('copy_customers.csv', 'w') as a_writer:
    reader = csv.reader(a_reader)
    for row in reader:
        csv_writer = csv.writer(a_writer)
        csv_writer.writerow(row)
