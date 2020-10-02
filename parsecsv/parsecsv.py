import csv

counts = dict()

with open("CS50.csv", "rt") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        title = row["title"]
        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1

    for title, count in counts.items():
        print(title, count, sep= " | ")
