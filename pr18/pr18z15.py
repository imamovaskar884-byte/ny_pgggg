# 15. Работа с CSV через with
import csv
with open('data.csv', 'r', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)