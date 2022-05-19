from itertools import islice
import sys

program, *args = sys.argv

total_lines = sum(1 for _ in open('bakery.csv', 'r'))

if len(args) > 1:
    start = int(args[0])
    stop = int(args[1])
    if stop > total_lines:
        exit(f'Ошибка. В файле всего {total_lines} строк')
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(*islice(f, start-1, stop))
elif len(args) == 1:
    start = int(args[0])
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(*islice(f, start-1, None))
else:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())
