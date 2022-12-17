import sqlite3

class Database:
    def __init__(self,db):   # db : table name
        self.con=sqlite3.connect(db)  # create a connection - con
        self.cur=self.con.cursor()  # create cursor object. it is used for create a table querys

        sql="""
        CREATE TABLE IF NOT EXISTS employees(
            id integer Primary key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        )
        """
        self.cur.execute(sql)  # execute used for pass querys.  exp:(sql)
        self.con.commit()    # commit() is used to commit your connection


    #insert function:
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name,age,doj,email,gender,contact,address))
        self.con.commit()


    #fetch all data from db:
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()    # rows used for fetch datas
        #print(rows)
        return rows

    # Delete a record in db:
    def remove(self,id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cur.execute("update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, email, gender, contact, address, id))
        self.con.commit()




#o=Database("Employee.db")
#o.insert("frank","23","12-03-2020","dinesh@gmail.com","male","7604959878","coimbatore")
#o.remove("3")  # remove items in a table
#o.fetch()  #show all records
#o.update("1","Jaculin","23","12-03-2020","Jacklin@gmail.com","female","7604939868","chennai")