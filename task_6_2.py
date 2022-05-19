result = []
with open('nginx_logs_small.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cur_line = line.split(' ')
        result.append((cur_line[0], cur_line[5][1:], cur_line[6]))
print(result)


ip_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ip_address = line.split(' ')[0]
        if ip_dict.get(ip_address):
            ip_dict[ip_address] += 1
        else:
            ip_dict[ip_address] = 1

max_requests = max(ip_dict.values())
ip_spam = [key for key, val in ip_dict.items() if val == max_requests]
print(f'Max requests {max_requests} was sent from following IP {ip_spam}')
