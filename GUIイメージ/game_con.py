from game_gui import *

def display():
    window = create_window()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "title":
            flg = event
            break

    window.close()
    return event