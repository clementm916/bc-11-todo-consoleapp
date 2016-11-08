import click
@click.group(help ="list command group")
def mylist():
	print ("listing items!!")
    
@mylist.command(help="list my items")
def items():
	pass