logins = []
LOGINS = []
EMAILS = {}

with open("login.txt") as file_handler:
    for line in file_handler:
        logins.append(line + '\n')
        line = line.split(' ')
        LOGINS.append(line[0].replace('\n', ''))
        EMAILS[line[1].replace('\n', '')] = line[0].replace('\n', '')
print(EMAILS)


def add_account(name, password, email):
    logins.append('{}:{} {}\n'.format(name, password, email))
    LOGINS.append('{}:{}'.format(name, password))
    EMAILS[email] = ['{}:{}'.format(name, password)]
    with open("login.txt", "w+") as file1:
        file1.writelines(logins)
