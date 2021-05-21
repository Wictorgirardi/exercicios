from datetime import datetime
import re


birthday = datetime.strptime('1997-01-03T00:00+0000', r'%Y-%m-%dT%M:%S%z')

regex = r'(\d{4}-\d{2}-\d{2})(T\d{2}:\d{2}\d{0,2})(\+\d{2}\:\d{2})?'
regex = re.compile(regex)

dates = []

with open("output-re-grp.txt", 'r') as f:
    content = f.read()

for date in regex.finditer(content):
    dt, hour, tz = date.groups()
    if tz:
        date = datetime.strptime(f'{dt}{hour}{tz}', r'%Y-%m-%dT%M:%S%z')
    else:
        date = datetime.strptime(f'{dt}{hour}+0000', r'%Y-%m-%dT%M:%S%z')
    dates.append(date)

results = []

for date in dates:
    results.append(abs(birthday - date))

min_result = min(results)
index = results.index(min_result)
nearest_date = dates[index]

print("Birthday:", birthday)
print("Nearest date:", nearest_date)
