from .cui_title import *

def con_title():
    root = cui_title()
    while True:
        root.strset("Here is cui_titleWindow..","Please select next..","1.game","2.log","3.setting")
        print(root.root)
        x = input()

        if x == '1':
            return 'game'
        if x == '2':
            return 'log'
        if x == '3':
            return 'setting'
