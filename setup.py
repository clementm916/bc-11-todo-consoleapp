from setuptools import setup, find_packages

setup(
    name='todo',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'python-firebase',
        'tabulate',
        'colorama',
        'pyfiglet'
    ],
    entry_points='''
        [console_scripts]
        todo=todo.scripts.main:Todo.todo
        open=todo.scripts.main:Todo.open
        create=todo.scripts.main:Todo.create
        list=todo.scripts.main:Todo.mylist
        items=todo.scripts.main:Todo.items
        item=todo.scripts.main:Todo.item
        add=todo.scripts.main:Todo.add
        cli=todo.scripts.main:Todo.cli
        start_todo = todo.scripts.main:Todo.run_app

      ''',
)