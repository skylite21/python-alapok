

import unicodedata
names = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

users = [
    {
        'name': ['Kovács', 'Béla'],
        'email': 'kovacs.bela@company.hu',
        'password':'Kovács123Start'
    },
    {
        'name': ['Kiss', 'Gyula'],
        'email': 'kiss.gyula@company.hu',
        'password':'Kiss123Start'
    },
    {
        'name': ['Szabó', 'Ervin'],
        'email': 'szabo.ervin@company.hu',
        'password':'Szabó123Start'
    },

]


data = 'Szabó béláaáá145úúő'
normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
print(normal.decode("utf-8"))
