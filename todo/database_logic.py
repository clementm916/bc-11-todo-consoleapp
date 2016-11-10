#env/bin/python
import sqlite3
import datetime
from collections import OrderedDict
class MyTodo(object):
	
	def __init__(self):
		self.db = sqlite3.connect("data/todos.db")
		self.cursor = self.db.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS todoinfo(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TEXT,todo_name STRING UNIQUE)")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS iteminfo(id INTEGER PRIMARY KEY AUTOINCREMENT,added_at TEXT, item STRING,todo_id INTEGER,FOREIGN KEY(todo_id)REFERENCES todoinfo(id))")

	def add_todo(self,todo):
		try:
			time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %S"))
			self.cursor.execute("INSERT INTO todoinfo(created_at,todo_name) VALUES (?,?)",(time,todo))
			self.db.commit()
			return "Added successfully"
		except(sqlite3.IntegrityError):
			return -1

	def open_todo(self,todo):
		try:
			to_type =type(todo)
			if to_type == str:
				if self.cursor.execute("SELECT id from todoinfo WHERE  todo_name ='%s'" %todo):
					self.is_open =True
					self.open_point = self.cursor.fetchone()[0]
					return self.open_point
			elif to_type==int:
				if self.cursor.execute("SELECT id from todoinfo WHERE id =%d" %todo):
					self.open_point = self.cursor.fetchone()[0]
					self.is_open =True
					return self.open_point
			elif to_type==list:
				if self.cursor.execute("SELECT id from todoinfo WHERE id =%d " %todo[0]):
					self.is_open =True
					self.open_point = self.cursor.fetchone()[0]
					return self.open_point
			else:
				return -1
		except(TypeError):
			return -1


	def add_item(self, item,todo):
		todo_id =self.open_todo(todo)
		time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %S"))
		self.cursor.execute("INSERT INTO iteminfo(added_at,item,todo_id) VALUES (?,?,?)",(time,item,todo_id))
		self.db.commit()


	def fetch_list(self,todo):
		try:
			todo = int(todo)
		except:
			pass
		cid =self.open_todo(todo)
		self.cursor.execute("SELECT id, added_at,item from iteminfo WHERE todo_id=%d" %cid)
		all_rows =[]
		
		for row in self.cursor:
			myrow=OrderedDict()
			myrow['id']=row[0]
			myrow['created_at']=row[1]
			myrow['todo']= row[2]
			all_rows.append(myrow)
		if all_rows==[]:
			return -1
		else:
			return all_rows

	def fetch_lists(self):
		self.cursor.execute("SELECT id, created_at,todo_name from todoinfo")
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
	def ffb_todos(self):
		self.cursor.execute("SELECT id, created_at,todo_name from todoinfo")
		all_rows ={}
		
		for row in self.cursor:
			myrow={}
			myrow['created_at']=row[1]
			myrow['todo']= row[2]
			myrow['items']={}
			all_rows[row[0]]=myrow
			return all_rows
	def ffb_items(self):
		self.cursor.execute("SELECT id, added_at,item from iteminfo")
		all_rows =[]


sample = MyTodo()

print sample.ffb_todos()

