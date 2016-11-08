#env/bin/python
import sqlite3
import time
import datetime
from collections import OrderedDict
class MyTodo(object):
	def __init__(self):
		self.db = sqlite3.connect("todos.db")
		self.cursor = self.db.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS todoinfo(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TEXT,todo STRING)")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS iteminfo(id INTEGER PRIMARY KEY AUTOINCREMENT,added_at TEXT, item STRING,todo_id INTEGER,FOREIGN KEY(todo_id)REFERENCES todoinfo(id))")

	def add_todo(self,todo):
		time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %S"))
		self.cursor.execute("INSERT INTO todoinfo(created_at,todo) VALUES (?,?)",(time,todo))
		self.db.commit()

	def open_todo(self,todo):
		to_type =type(todo)
		if to_type == str:
			self.cursor.execute("SELECT id from todoinfo WHERE  todo =%s" %todo)
			return self.cursor.fetchones()[0]
		elif to_type==int:
			self.cursor.execute("SELECT id from todoinfo WHERE id =%d" %todo)
			return self.cursor.fetchone()[0]
		elif to_type==list:
			self.cursor.execute("SELECT id from todoinfo WHERE id =%d " %todo[0])
			return self.cursor.fetchone()[0]
		else:
			return -1



	def add_item(self, item,todo):
		todo_id =self.open_todo(todo)
		time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %S"))
		self.cursor.execute("INSERT INTO iteminfo(added_at,item,todo_id) VALUES (?,?)",(date,todo_id))

	def fetch_list(self,todo):
		cid =open_todo(todo)
		self.cursor.execute("SELECT id, added_at,item from iteminfo WHERE todo_id=cid")

	def fetch_lists(self):
		self.cursor.execute("SELECT id, created_at,todo from todoinfo")
		all_rows =[]
		
		for row in self.cursor:
			myrow=OrderedDict()
			myrow['id']=row[0]
			myrow['created_at']=row[1]
			myrow['todo']= row[2]
			all_rows.append(myrow)
		return all_rows
	def fetch_item(self):
		self.cursor.execute("SELECT id, created_at,item from iteminfo")
		print (self.cursor.lastrawid)
	def delete_list(self):
		pass

	def delete_item(self,id):

		self.cursor.execute("DELETE from itemsinfo where ID=id;")

test = MyTodo()
test.add_todo("Today")

print test.cursor.lastrowid

test.open_todo(5)

print test.open_todo(1)

#sqlite3.OperationalError: no such column: Today