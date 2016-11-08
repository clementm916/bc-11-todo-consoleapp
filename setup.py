from setuptools import setup, find_packages

setup(
    name='todopackage',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'python-firebase',
        'tabulate',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        todopackage=todopackage.scripts.script:todo
        todo=todopackage.scripts.script:todo
        open=todopackage.scripts.script:open
        create=todopackage.scripts.script:create
        list=todopackage.scripts.script:mylist
        items=todopackage.scripts.script:items
        item=todopackage.scripts.script:item
        add=todopackage.scripts.script:add
        cli=todopackage.scripts.script:cli

      ''',
)