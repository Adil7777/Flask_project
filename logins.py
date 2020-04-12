LOGINS = []

with open("logins.txt") as file_handler:
    for line in file_handler:
        LOGINS.append(line.replace('\n', ''))

print(LOGINS)
