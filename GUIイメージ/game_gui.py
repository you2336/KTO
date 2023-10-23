import PySimpleGUI as sg

def create_window():
    layout = [[sg.Text("Here is game",size=(10,2))],[sg.Button("back",key='title')],]
    
    window = sg.Window("Exit Example", layout)

    return window

if __name__ == "__main__":
    create_window()