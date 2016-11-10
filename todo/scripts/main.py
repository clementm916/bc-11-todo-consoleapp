import click
import time
from tabulate import tabulate
from pyfiglet import Figlet
from inspect import getsourcefile
from . string_to_list import stringToList
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)
from .access_var import readStatus,writeStatus,writeLastOpen,readLastOpen
from database_logic import MyTodo

from progress_bar import printProgress,playSpinner,spinningCursor
from colorama import init,Fore, Back, Style
init(autoreset=True)

myDb = MyTodo()


class Todo(object):
	@click.group()
	def todo():
		pass

	@todo.command(help="Creates a todo list")
	@click.argument('todo_name',nargs =1)
	def create(todo_name):
		creating = myDb.add_todo(todo_name)
		playSpinner()
		if creating == -1:
			print(Fore.RED +"\t\tNot added: The todo name already exists.")
		else:
			print(Fore.GREEN + creating)



	@todo.command(help ="Opens a todo list")
	@click.argument('to-read',default=None)
	def open(to_read):
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

		todos=myDb.fetch_lists()

		from time import sleep

		# make a list
		items = range(len(todos)*5)
		i= 0
		l= len(items)

		# Initial call to print 0% progress
		printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)
		for item in items:
			sleep(0.4)
			# Update Progress Bar
			i += 1
			printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)

		print(tabulate(todos, headers='keys', tablefmt="fancy_grid"))
		

	@click.group()
	def item(help="Item group command"):
		pass

	@item.command(help ="Add an item to a list")
	@click.argument('item_toadd')
	def add(item_toadd):
		is_open = readStatus()
		playSpinner()
		todo =readLastOpen()
		if not is_open == "True":
			print(Fore.RED + "\t\tNo open todo to add your items")    
		else:
			print ("Adding "+ item_toadd, end ="")
			playSpinner()
			myDb.add_item(item_toadd,todo)

	@item.command(help = "List items ")
	@click.argument('todo_name',nargs =1)
	def list(todo_name):
		pass

	@click.group(help ="list command group")
	def mylist():
		pass
	    
	@mylist.command(help="lists items in a todo list")
	@click.argument('todo_name',nargs =1)
	def items(todo_name):
		
		it = myDb.fetch_list(todo_name)
		if it == -1:
			playSpinner()
			print(Fore.RED+ "Given todo has no Items")
		else:
			items = range(len(it)*5)
			i= 0
			l= len(it)

			# Initial call to print 0% progress
			printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)
			for item in items:
				sleep(0.4)
				# Update Progress Bar
				i += 1
				printProgress(i, l, prefix = 'Fetching:', suffix = 'Complete', barLength = 50)
			print(tabulate(it, headers='keys', tablefmt="fancy_grid"))
	@click.command()
	def run_app():
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
		print(Fore.BLUE + "item ",end=" ")
		print(Fore.BLUE + "<todo-name or todo-id>")


		