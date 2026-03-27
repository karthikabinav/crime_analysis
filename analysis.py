import csv

total = {}
arrested = {}

with open('/data/Crime_records.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Date_Reported'].startswith('2020'):
            gender = row['Suspect_Gender']
            total[gender] = total.get(gender, 0) + 1
            if row['Arrest_Made'] == 'Yes':
                arrested[gender] = arrested.get(gender, 0) + 1

print('Total by gender:', total)
print('Arrested by gender:', arrested)
