from unittest import TestCase
from app.todoitem import TodoItem
from data import schema, seed
from os import remove

# run this to run any tests
# python3 -m unittest discover tests

TodoItem.dbpath = "test.db"

class TestTodoItem(TestCase):
    dbpath = "test.db"
    def setUp(self): #at the start of each test do something in this case populate a database
        schema.schema(dbpath = "test.db")
        seed.seed(dbpath = "test.db")
        

    def tearDown(self): #after each test do something in this case delete the database
        remove("test.db")

    def testCreation(self):
        todo = TodoItem(pk = 1, title = "title", description = "desc", complete = 0)
        self.assertIsInstance(todo, TodoItem, "__init__ returns a TodoItem")
        self.assertEqual("title", todo.title)
    
    def testSelectOne(self):
        todo = TodoItem.select_one(1)
        self.assertIsInstance(todo, TodoItem, "select_one returns a TodoItem")
        self.assertEqual("test.db", todo.title)

    def testInsert(self):
        todo = TodoItem(title = "title", description = "desc", complete = 0)
        todo._insert()
        saved_todo = TodoItem.select_one(2)
        self.assertEqual("title", saved_todo.title)

    def testSave(self):
        todo = TodoItem(title = "t", description = "d", complete = 0)
        todo.save()
        saved_todo = TodoItem.select_one(2)
        self.assertEqual("t", saved_todo.title)

        change = TodoItem.select_one(1)
        change.title = "Nottitle"
        change.save()
        saved_todo = TodoItem.select_one(1)
        self.assertEqual("Nottitle", saved_todo.title)

    def testUpdate(self):
        change = TodoItem.select_one(1)
        change.title = "NotNottitle"
        change._update()
        saved_todo = TodoItem.select_one(1)
        self.assertEqual("NotNottitle", saved_todo.title)

    def testSelectAll(self):
        todo = TodoItem(title = "t", description = "d", complete = 0)
        todo.save()
        todo1 = TodoItem(title = "title", description = "desc", complete = 0)
        todo1.save()
        saved_todo = TodoItem.select_all()
        self.assertEqual(3, len(saved_todo))


    def testDelete(self):
        todo = TodoItem.select_one(1)
        todo.delete()
        saved_todo = TodoItem.select_all()
        self.assertEqual(0,len(saved_todo))

    def testRepr(self):
        todo = TodoItem.select_one(1)
        statement = todo.__repr__
        self.assertIn("<TodoItem: pk=1>",str(statement))


