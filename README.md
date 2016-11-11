# Todo App (Nitafanya)
Todo is a console application that lets a user to create a todo list and add items to the list.A todo is a list of things the user wants to do and an item is an activity in the todo list. The user is able to view a list of their todos as well as a list of of the items in a given todo. Using this app a user should be able to add "todo lists" and add items to them. They should also be able to view what they have added.


# Installation
Todo app is a python package and can be installed as such. First setup a virtual environment where the application's dependencies will be automatically installed:
```sh
$ pip install virtualenv          #install virtualenv module
$ virtualenv to-do                #setup your own virtual env
$ source to-do/bin/activate #to activate environment in linux, in windows run to-do/scripts/activate
```
To install the app, clone this repository: 
```sh
$ git clone https://github.com/clementm916/bc-11-todo-consoleapp
$ cd bc-11-todo-consoleapp
$ pip install -editable .           #this installs the app and all required modules
```

# Setting Up
Todo was developed with Python version `3.5`  therefore may not work properly on previous versions(python 2). Start the application in   using the following command:
```sh
$ start_todo #this is the first command you should run in the application 
Starting app ....                        
  #compressed branding display                    
The following are the avaibale app commands for use :
Creating a list of Todo items : 
  todo  create <name-of-the-todo-list>
Adding an Item to a list : 
  todo open <name-of-the-todo-list> <or [Index of the todo-list]>
  item add <name-of-the-item> 
List all todos : 
  todo list 
List all items within a todo : 
  list items  <todo-name or todo-id>

```

# Functionality
### `--help` option
This is to help the user whenever they have trouble using a given command:
```sh
$ items --help
Usage: items [OPTIONS] TODO_NAME

  lists items in a todo list

Options:
  --help  Show this message and exit.
```
### `start_todo` command
First command you should run on installing the applicaton.Sets up the application and  provides with you with a summary of the available commands.
```sh
$ start_todo
Starting app ....                        
                        
#compressed branding display
                                                     
The following are the avaibale app commands for use :
Creating a list of Todo items : 
	todo  create <name-of-the-todo-list>
Adding an Item to a list : 
	todo open <name-of-the-todo-list> <or [Index of the todo-list]>
	item add <name-of-the-item> 
List all todos : 
	todo list 
List all items within a todo : 
	list items  <todo-name or todo-id>

```

### `todo` command
This is a base command with several sub-commands
```sh
$ todo --help
Usage: todo [OPTIONS] COMMAND [ARGS]...

  Defining the group command "todo"

Options:
  --help  Show this message and exit.

Commands:
  create  Creates a todo list
  list    Lists todo lists
  open    Opens a todo list
  sync    Synchronize data to firebase
```


### `create` command
To create a new todo list:
```sh
$ todo create --help
Usage: todo create [OPTIONS] TODO_NAME

  Creates a todo list
  #example
$ todo create "Books to read"

```

### `todo list` command
```sh
#view available lists
$ todo list
Fetching: |██████████████████████████████████████████████████| 100.0% Complete
╒══════╤═════════════════════╤══════════════════╕
│   id │ created_at          │ todo             │
╞══════╪═════════════════════╪══════════════════╡
│    1 │ 2016-11-10 23:05 39 │ Todo on Friday   │
├──────┼─────────────────────┼──────────────────┤
│    2 │ 2016-11-10 23:07 27 │ Todo on Saturday │
├──────┼─────────────────────┼──────────────────┤
│    3 │ 2016-11-10 23:07 48 │ Books to read    │
╘══════╧═════════════════════╧══════════════════╛
```

### `todo open | list items` commands
To add items to the todo list you have to open the todo list you want to add items to. Otherwise you get an error. If you open two lists. The second one closes the first one. So any items you add are added to the todo list.
```sh
#adding an item to the third item, you can pass the id or the name
$ todo open [3]                     #don't forget to open it first todo open "Books to read " would work in a similar way.
 Opened [3] successfully You can now add items using item add <item-name>
#then add the items
$ item add "A byte of python"
```
### `list items` command
This command lists all items in a given todo list
```sh
$ list items --help
Usage: list items [OPTIONS] TODO_NAME
   returns items in a todo list
 
#example
$ list items "Books to read"
Fetching: |██████████████████████████████████████████████████| 100.0% Complete
╒══════╤═════════════════════╤═══════════════════════════╕
│   id │ created_at          │ item                      │
╞══════╪═════════════════════╪═══════════════════════════╡
│    1 │ 2016-11-10 23:20 16 │ C how to program          │
├──────┼─────────────────────┼───────────────────────────┤
│    2 │ 2016-11-10 23:23 10 │ A byte of python          │
├──────┼─────────────────────┼───────────────────────────┤
│    3 │ 2016-11-10 23:24 12 │ Introduction to Algorthms │
├──────┼─────────────────────┼───────────────────────────┤
│    4 │ 2016-11-10 23:27 29 │ Java black book           │
╘══════╧═════════════════════╧═══════════════════════════╛


```

# To Do

  * Edit todos
  * Edit items
