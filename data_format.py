# csvファイルを扱う
# import csv

# with open('sample.csv', mode='r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# with open('sample.tsv', mode='r') as f:
#     reader = csv.reader(f, delimiter='\t', quotechar='#')
#     for row in reader:
#         print(row)

# with open('sample.csv', mode='r', encoding='utf-8') as read_file:
#     reader = csv.reader(read_file)
#     next(reader)

#     with open('result.tsv', newline='', mode='w', encoding='utf-8') as write_file:
#         writer = csv.writer(write_file, delimiter='\t')

#         writer.writerow(['都道府県', '人口密度（人/km2）'])

#         for row in reader:
#             populationo_density = float(row[2]) / float(row[3])
#             writer.writerow([row[1], int(populationo_density)])

# JSONを扱う
import json
data = [{'id': 123, 'entities': {'url': 'python.org',
                                 'hashtags': ['#python', '#pythonjp']}}]
# print(json.dumps(data, indent=2))
print(json.dumps(data, indent=4, sort_keys=True))
