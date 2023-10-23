from title_gui import *

window_set = {
    "setting",
    "game",
    "log"
}

def display():
    window = create_window()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event in window_set:
            break

    window.close()
    return event