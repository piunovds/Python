import sys

program, incom, *args = sys.argv

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f'{incom}\n')
