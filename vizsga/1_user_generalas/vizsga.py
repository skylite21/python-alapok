import unicodedata

data = 'Szabó béláaáá145úúő'
normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
print(normal.decode("utf-8"))

names = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]


users = []

for name in names:
    name_dict = {}
    name_dict['name'] = name
    email = []
    for n in name:
        acc_removed = unicodedata.normalize('NFKD', n).encode(
            'ASCII', 'ignore').decode('utf-8')
        acc_removed = acc_removed.lower()
        email.append(acc_removed)
    name_dict['email'] = '.'.join(email)+'@company.hu'
    name_dict['password'] = name[0]+'123Start'
    users.append(name_dict)

with open('nevek.txt', 'w') as f:
    for user in users:
        line = ' '.join(user['name'])
        line += ' '+user['email']
        line += ' '+user['password']
        line += '\n'
        f.write(line)

print(users)
