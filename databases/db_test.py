
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="my_db_user",
    password="12345",
    database="my_first_database"
)

c = mydb.cursor()
c.execute(
    "create table if not exists vasarlok (vasarlo_neve varchar(255), vasarlo_cime varchar(255))")


c.execute(
    "insert into vasarlok (vasarlo_neve, vasarlo_cime) values ('Peter', 'Gödöllő')")

c.execute("select * from vasarlok")

my_result = c.fetchall()

for e in my_result:
    print(e)
