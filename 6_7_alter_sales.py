from itertools import islice
import sys

program, *args = sys.argv

if len(args) < 2:
    exit(f'Ошибка. Ожидается два парамера: номер записи и новое значение')

total_lines = sum(1 for _ in open('bakery.csv', 'r'))
line_number = int(args[0])
value = args[1]

if line_number > total_lines:
    exit(f'Ошибка. В файле всего {total_lines} строк')

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    current_line = 1
    line = f.readline()
    while line:
        if current_line == line_number-1:
            f.seek(f.tell())
            f.write(value)
            break
        current_line += 1
        line = f.readline()
