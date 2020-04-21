import csv

with open("rectangles.csv", newline='') as fajl:
    reader=csv.reader(fajl)
    header=next(reader)

    data=[]

    for row in reader:
        a=int(row[0])
        b=int(row[1])
        if a==b:
            data.append(a*b)

    print(max(data))