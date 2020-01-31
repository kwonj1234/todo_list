#In Java, Data Access Object
#ORM, Object Relational Mapper, is a more general term
#Basically an object oriented (class) program that accesses the database

import sqlite3
import os

class TodoItem:
    dbpath = ""
    tablename = "todoitems"
    #You want these to be class attributes because these will never change

    def __init__(self, **kwargs): #kwargs is a dictionary kwargs : keyword arguments
        self.pk = kwargs.get("pk")
        self.title = kwargs.get("title")
        self.description = kwargs.get("description")
        self.complete = kwargs.get("complete")

#which one is an instance method or class method?
    def save(self):
        if self.pk is None: #None, True, False are already stored in memory so you can use "is"
            self._insert()
        self._update()

    def _insert(self): #the underscore makes things a private method
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """INSERT INTO {} (title, description, complete)
                VALUES (?,?,?);""".format(self.tablename)
            curs.execute(sql, (self.title, self.description, self.complete))

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            sql = """UPDATE {} SET title = ?, description = ?, complete = ?
                WHERE pk=?;""".format(self.tablename)

            values = (self.title, self.description, self.complete, self.pk)
            curs.execute(sql, values)
    #insert and update are essentially save operations
    #insert saves something new
    #update overwrites and saves

    def delete(self):
        with sqlite3.connect(self.dbpath) as conn:
            curs = conn.cursor()
            
            sql = """DELETE FROM {} WHERE pk = ?;""".format(self.tablename)

            curs.execute(sql, (self.pk,))

    @classmethod
    def select_all(cls, complete = None):
        """select all entries from our database based on whether they are complete or not,
        or selects all if complete = None"""
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row #make into dictionary formats
            curs = conn.cursor()
        
            if complete is None:
                sql = """SELECT * FROM {};""".format(cls.tablename)
                curs.execute(sql)
            else:
                sql = """SELECT * FROM {} WHERE complete = ?;""".format(cls.tablename)
                curs.execute(sql, (complete,))
            # return curs.fetchall()

            rows = curs.fetchall()   #make into list formats
            return [cls(**row) for row in rows]

    @classmethod
    def select_one(cls, pk):
        """selects an entry from our database based on a pk"""
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            curs = conn.cursor()
            sql = f"""SELECT * FROM {cls.tablename} WHERE pk =?;"""
            curs.execute(sql, (pk,)) #don't forget to put a comma after single value inputs
            row = curs.fetchone()
            return cls(**row)

    def __repr__(self):
        return f"<TodoItem: pk={self.pk}>"
        