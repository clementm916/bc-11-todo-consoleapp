import click
@click.group()
def item(help="Item group command"):
	pass

@item.command(help ="Add an item to a list")
def add():
	pass
@item.command(help = "List items ")
def list():
	pass