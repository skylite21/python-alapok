
players = []
with open('./jatekosok.txt', 'r') as f:
    for line in f:
        # sorvége jeleket (entereket: \n karaktert...)
        # leszedjük a sorok végéről:
        line = line.strip()
        # szétbontjuk a sort, listává alakítjuk, a delimiterünk
        # a szóköz
        player_list = line.split(' ')
        # létrehozunk egy dictionary-t
        # meghatározott key-ekkel, a value-k pedig
        # a lista aktuális eleme..
        player = {"name": player_list[0],
                  "age": int(player_list[1]),
                  "nationality": player_list[2],
                  "score": int(player_list[3])}
        # hozzáfűzzük a player dictionary-t a players listához
        players.append(player)

print(players)

nationalities = set()
for player in players:
    nationalities.add(player['nationality'])

# az előző sor set comprehension-el
# nationalities = {player['nationality'] for player in players}
print(nationalities)

scores = {}
for nationality in nationalities:
    # létrehozzuk a scores dictionaryben az új nationality-t nulla értékkel
    scores[nationality] = 0
    for player in players:
        if player['nationality'] == nationality:
            # scores[nationality] = scores[nationality] + player['score']
            scores[nationality] += player['score']

print(scores)

underage = []
for player in players:
    if player['age'] < 20:
        underage.append(player)
print(underage)
print("a kiskorúak száma: {}".format(len(underage)))


# [['English', 101], ['Hungarian', 90]...]
# házi feladat: készítsd el az eredmény kihirdetést,
# és írd ki az eredményt egy file-ba, az eredmeny.txt file
# tartalma:
# 1. English: 101
# 2. Hungarian: 90
# 3. Spanish:  49
