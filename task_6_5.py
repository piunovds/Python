import sys

program, users_file, hobby_file, output_file, *args = sys.argv

user_lines = sum(1 for line in open(users_file, 'r'))
hobby_lines = sum(1 for line in open(hobby_file, 'r'))
if user_lines < hobby_lines:
    exit("1")

with open(users_file, 'r', encoding='utf-8') as f_users:
    with open(hobby_file, 'r', encoding='utf-8') as f_hobby:
        with open(output_file, 'w', encoding='utf-8') as f_users_hobby:
            for user_line in f_users:
                hobby_line = f_hobby.readline()
                if hobby_line:
                    f_users_hobby.write(f'{user_line.strip()}: {hobby_line.strip()}\n')
                else:
                    f_users_hobby.write(f'{user_line.strip()}: None\n')
