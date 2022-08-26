import csv 

data = [row for row in csv.reader(open("pima-indians-diabetes.csv"))]
data = [list(map(lambda x: float(x), row)) for row in data[1:] if "" not in row]
data = filter(lambda row: row[1] > 0 and row[2] > 0 and row[3] > 0 and row[4] > 0, data)
rv = [row[1:5] for row in data][:10]
print(rv)
