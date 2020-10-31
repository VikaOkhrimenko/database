import sqlite3

max_salary = 10000

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

def adduser(name, surname, salary):
    c.execute("insert into users (name, surname, salary) values ('%s', '%s', '%s')" %(name, surname, salary))
    conn.commit()


name = input("Enter user name: ")
surname = input("Enter user surname: ")
salary = input("Enter user salary: ")

while float(salary) > max_salary:
    salary = input("The maximum salary is 10000, you enter a big salary.Enter other salary: ")

adduser(name, surname, salary)

print("Users list: \n")
c.execute('select * from users')
ulist = c.fetchone()

while ulist is not None:
    print("id: "+str(ulist[0]) + " Name: "+str(ulist[1]) + " Surname: "+str(ulist[2])+ " Salary: "+str(ulist[3]))
    ulist = c.fetchone()

c.close()
conn.close()