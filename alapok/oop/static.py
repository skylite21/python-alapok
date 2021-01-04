class Date:
    def __init__(self, date):
        self.date = date

    # metódus csak objektum példányon futtatható
    def get_date(self):
        return self.date

    # status metódus v. class metódus: olyan metódus ami az osztályon
    # futtatható közvetlenül, és nem kell hozzá példány
    @staticmethod
    def to_dash_date(date):
        return date.replace('/', '-')


date = Date('2021-01-04')
print(date.get_date())

date_from_db = '2021/01/01'

# print(date.to_dash_date(date_from_db))
print(Date.to_dash_date(date_from_db))
