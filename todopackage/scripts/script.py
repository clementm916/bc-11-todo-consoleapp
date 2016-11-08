import click
from tabulate import tabulate

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from model import MyTodo
from colorama import init,Fore, Back, Style
init(autoreset=True)

oohmy = MyTodo()



@click.group()
def todo():
	pass

@todo.command(help="Creates a todo list")
@click.argument('todo_name',nargs =1)
def create(todo_name):

	oohmy.add_todo(todo_name)



@todo.command(help ="Opens a todo list")
@click.argument('to-read')
def open(to_read,):
	oohmy.open_todo(to_read)
	print("Opened "+ to_read)
@todo.command(help="Lists todo lists\n")
def list():
	print(Fore.GREEN+"Listing to do lists")
	todos=oohmy.fetch_lists()
	print(tabulate(todos, headers='keys', tablefmt="fancy_grid"))
	

@click.group()
def item(help="Item group command"):
	pass

@item.command(help ="Add an item to a list")
@click.argument('item_toadd')
def add(item_toadd):
	print (oohmy.cursor)
	print ("Adding "+ item_toadd)
@item.command(help = "List items ")
@click.argument('todo_name',nargs =1)
def list(todo_name):
	pass

@click.group(help ="list command group")
def mylist():
	print ("listing items!!")
    
@mylist.command(help="list my items")
@click.argument('todo_name',nargs =1)
def items(todo_name):
	oohmy.fetch_list(todo_name)
