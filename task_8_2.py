import re

def parserr(line):
    regexp_list = [r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
                   r'\[(.*?)\]',
                   r'\"([A-Z]{3})',
                   r'\s(\/[\w\/]+)',
                   r'\s(\d{3})\s',
                   r'\s\d{3}\s(\d+)']
    return tuple(re.findall(reg, line)[0] for reg in regexp_list)


with open('nginx_logs.txt') as f:
    count = 2000
    line = f.readline()
    while count and line:
        print(parserr(line))
        count -= 1
        line = f.readline()
