import mysql.connector

dbConnecter = mysql.connector.connect(
    host='localhost',
    user='vikash',
    passwd='rrsv',
    database="APP"
)

db = dbConnecter.cursor()

db.execute('CREATE TABLE Ex_one (id INT AUTO_INCREMENT,name VARCHAR(100), description TEXT, category_id INT(50), chef_id INT(20), created DATETIME, PRIMARY KEY(id))')

for x in db:
    print(x)
