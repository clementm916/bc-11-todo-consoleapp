#env/bin/python
import sqlite3
import datetime
from collections import OrderedDict
class MyTodo(object):
	
	def __init__(self):
		""" 
		Initialises MyTodo obejct
		"""
		self.is_open = None
		self.open_point = None
		self.db = sqlite3.connect("data/todos.db")
		self.cursor = self.db.cursor()
		self.cursor.execute("CREATE TABLE IF NOT EXISTS todoinfo(id INTEGER PRIMARY KEY AUTOINCREMENT,created_at TEXT,todo_name STRING UNIQUE)")
		self.cursor.execute("CREATE TABLE IF NOT EXISTS iteminfo(id INTEGER PRIMARY KEY AUTOINCREMENT,added_at TEXT, item STRING,todo_id INTEGER,FOREIGN KEY(todo_id)REFERENCES todoinfo(id))")

	def add_todo(self,todo):
		"""
		Add a todo to the database
		@params
			todo -> the todo to be created/added to db
		"""
		try:
			time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %S"))
			self.cursor.execute("INSERT INTO todoinfo(created_at,todo_name) VALUES (?,?)",(time,todo))
			self.db.commit()
			return "Added successfully"
		except(sqlite3.IntegrityError):
			return -1

	def open_todo(self,todo):
		"""
		Aids in opening a todo for adding data to it.
		@params
			todo -> the todo to be opened
		"""
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
		""" 
		Adds an item to an open todo.
		@params
		item -> item to be added
		todo -> the list to add the item to

		"""
		todo_id =self.open_todo(todo)
		time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %S"))
		self.cursor.execute("INSERT INTO iteminfo(added_at,item,todo_id) VALUES (?,?,?)",(time,item,todo_id))
		self.db.commit()


	def fetch_list(self,todo):
		"""
		Returns the items in a todo list
		@params
			todo -> the todo to return its items 
		"""
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
		"""
		Returns all the lists in the database

		"""
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
	def delete_list(self,list_id):
		""" 
		Deletes a list from the database

		"""
		self.cursor.execute("DELETE from todoinfo where id=%d"%list_id)

	def delete_item(self,item_id):
		"""
		Deletes an item from the database

		"""
		self.cursor.execute("DELETE from itemsinfo where ID=%d"%item_id)
