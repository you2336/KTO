import PySimpleGUI as sg

def create_window():
    layout = [[sg.Text("Here is title",size=(10,2))],
              [sg.Button("setting",key='setting')],[
                  sg.Button("game",key='game',size=(10,2))],
              [sg.Button("log",key='log')],]
    
    window = sg.Window("Exit Example", layout)

    return window

if __name__ == "__main__":
    create_window()