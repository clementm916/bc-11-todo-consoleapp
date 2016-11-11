import click
import time
from tabulate import tabulate
from pyfiglet import Figlet
from inspect import getsourcefile
from colorama import init,Fore, Back, Style
init(autoreset=True)

import sys

"""
Own written imports
"""

from .access_var import readStatus,writeStatus,writeLastOpen,readLastOpen
from todo.database_logic import MyTodo
from todo.fire_base import synchronize
from . string_to_list import stringToList
from . progress_bar import printProgress,playSpinner,spinningCursor


#db object for use
myDb = MyTodo()


class Todo(object):
	@click.group()
	def todo():
		"""
		Defining the group command "todo"

		"""
		pass

	@todo.command(help="Creates a todo list")
	@click.argument('todo_name',nargs =1)
	def create(todo_name):
		"""
		Defining create command which takes a todo_name and creates the repctive todo

		@params 
		todo_name -> nmae of the todo to be created

		"""
		creating = myDb.add_todo(todo_name)
		playSpinner()
		if creating == -1:
			print(Fore.RED +"\t\tNot added: The todo name already exists.")
		else:
			print(Fore.GREEN + creating)



	@todo.command(help ="Opens a todo list")
	@click.argument('to-read',default=None)
	def open(to_read):
		"""
		Defining open command which opens a file for reading

		@params
		to_read -> the list to be read

		"""
		try:
			to_read = int(to_read)
		except (ValueError):
			pass
		print ("Opening ", end ="")
		spinner = spinningCursor()
		for _ in range(16):
		    sys.stdout.write(next(spinner))
		    sys.stdout.flush()
		    time.sleep(0.1)
		    sys.stdout.write('\b')

		if not stringToList(to_read) == -1:
			to_read = stringToList(to_read)
		is_open = readStatus()
		if is_open == "True":
			writeStatus("False")
		if not myDb.open_todo(to_read) == -1:
			opened = myDb.open_todo(to_read)
			writeLastOpen(opened)
			writeStatus("True")
			print(Fore.GREEN + "Opened " + str(to_read)+" successfully ",end="")
			print(Fore.BLUE +"You can now add items using ", end="")
			print(Fore.YELLOW+ "item add <item-name>")
		
		else:

			print(Fore.RED + "\t\tFailed!! Requested Todo Not in Database")
	@todo.command(help="Lists todo lists\n")
	def list():
		"""
		command that returns all the lists in the database

		"""

		todos=myDb.fetch_lists()
		if len(todos)<5:
			ll= len(todos)*5
		else:
			ll =len(n)
		items = range(ll)
		i= 0
		l= len(items)

		# Initial call to print 0% progress
		printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)
		for item in items:
			time.sleep(0.1)
			# Update Progress Bar
			i += 1
			printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)

		print(tabulate(todos, headers='keys', tablefmt="fancy_grid"))

	
	@todo.command(help ="Synchronize data to firebase")	
	def sync():
		"""
		command to sync to a remote database 

		"""
		playSpinner
		print("Sychronizing to firebase")
		data = myDb.ffb_data() 
		synchronize(data)
		playSpinner

	@click.group()
	def item(help="Item group command"):
		"""
		defining item group command 
		"""
		pass

	@item.command(help ="Add an item to a list")
	@click.argument('item_toadd')
	def add(item_toadd):
		"""
		Adds an item to an open list.
		@params
			item_toadd -> item to be added to a list
		"""
		is_open = readStatus()
		playSpinner()
		todo =readLastOpen()
		if not is_open == "True":
			print(Fore.RED + "\t\tNo open todo to add your items")    
		else:
			print ("Adding "+ item_toadd)
			playSpinner()
			myDb.add_item(item_toadd,todo)

	@item.command(help = "List items ")
	@click.argument('todo_name',nargs =1)
	def list(todo_name):
		pass

	@click.group(help ="list command group")
	def mylist():
		"""
		list command group

		"""
		pass
	    
	@mylist.command(help="returns items in a todo list")
	@click.argument('todo_name',nargs =1)
	def items(todo_name):
		"""

		Returns the items in a todo list

		@params
		  todo_name -> name of the todo list to display it's items

		"""
		
		it = myDb.fetch_list(todo_name)
		if it == -1:
			playSpinner()
			print(Fore.RED+ "Given todo has no Items")
		else:
			if len(it)<5:
				ll =len(it) * 5
			else:
				ll = it
			items = range(ll)
			i= 0
			l= len(items)

			# Initial call to print 0% progress
			printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)
			for item in items:
				time.sleep(0.1)
				# Update Progress Bar
				i += 1
				printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)
			print(tabulate(it, headers='keys', tablefmt="fancy_grid"))
	@click.command()
	def run_app():
		"""

		sets up the application and gives a user guide

		"""
		print("Starting app ....",end="")
		playSpinner()
		writeStatus("None")
		writeLastOpen("None")
		f = Figlet(font='sans')
		print(Fore.GREEN + f.renderText('TODO'))
		print(Fore.BLUE + f.renderText('APPLICATION'))
		print(Fore.GREEN + "The following are the avaibale app commands for use :")
		print(Fore.YELLOW + "Creating a list of Todo items :",end=" ")
		print(Fore.CYAN + "\n\ttodo ",end=" ")
		print(Fore.BLUE + "create",end=" ")
		print(Fore.BLUE + "<name-of-the-todo-list>")

		print(Fore.YELLOW + "Adding an Item to a list :",end=" ")
		print(Fore.CYAN + "\n\ttodo",end=" ")
		print(Fore.BLUE + "open",end=" ")
		print(Fore.BLUE + "<name-of-the-todo-list>",end=" ")
		print(Fore.BLUE + "<or [Index of the todo-list]>")

		print(Fore.CYAN + "\titem",end=" ")
		print(Fore.CYAN + "add",end=" ")
		print(Fore.BLUE + "<name-of-the-item>",end=" ")
		print(Fore.BLUE + "")

		print(Fore.YELLOW + "List all todos :",end=" ")
		print(Fore.CYAN + "\n\ttodo",end=" ")
		print(Fore.BLUE + "list",end=" ")
		print(Fore.BLUE + "")

		print(Fore.YELLOW + "List all items within a todo :",end=" ")
		print(Fore.CYAN + "\n\tlist",end=" ")
		print(Fore.BLUE + "items ",end=" ")
		print(Fore.BLUE + "<todo-name or todo-id>")


		
