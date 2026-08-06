#!/usr/bin/env python3
import csv
import sys
from decimal import Decimal

with open(sys.argv[1], newline='', encoding='utf-8') as source:
    rows = csv.DictReader(source)
    total = sum((Decimal(row['amount']) for row in rows), Decimal('0'))
print(f'Total: {total:.2f} EUR')
