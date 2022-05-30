import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Dharsan",
    password="",
    database="Employee"  # step 2
)

practice1 = db.cursor()

# step 1 creating database
# practice1.execute("CREATE DATABASE Employee")

# step 3 creating a table in db
# practice1.execute("CREATE TABLE Employee (employee_id int PRIMARY KEY AUTO_INCREMENT, First_name VARCHAR(40), Last_name VARCHAR(40), email VARCHAR(40), phone_number CHAR, hire_date VARCHAR(10), Job_id int, salary int, manager_id int, department_id int)")

# displaying the table
practice1.execute("DESCRIBE Employee")

for x in practice1:
    print(x)

# adding values in table
practice1.execute("INSERT INTO Employee (First_name, Last_name, email, phone_number, hire_date, Job_id, salary, manager_id, department_id) VALUES ('Dharsan', 'S', 'dharsan@gmail.com', '9876543210', 07/05/2022, 101, 50000, 201, 301)")
practice1.commit()

# printing added values
practice1.execute("SELECT * FROM Employee")
for x in practice1:
    print(x)
