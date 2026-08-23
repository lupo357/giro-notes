#!/usr/bin/env python3
import argparse
import csv
from decimal import Decimal

parser = argparse.ArgumentParser(description='Add up a weekly receipt sheet.')
parser.add_argument('csv_file')
args = parser.parse_args()
with open(args.csv_file, newline='', encoding='utf-8') as source:
    rows = csv.DictReader(source)
    total = sum((Decimal(row['amount']) for row in rows if row['amount'].strip()), Decimal('0'))
print(f'Total: {total:.2f} EUR')
