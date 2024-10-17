import PySimpleGUI as sg
sg.theme_text_color("#00008B")
sg.theme_background_color("#FF4040")
window = sg.Window(title="Profile",
                  layout=[[sg.Text("NPM         : 2210010533 ")],
                          [sg.Text("Nama        : Muhammad Ridho Syahputra ")],
                          [sg.Text("Kelas        : 5M Regular Banjarmasin ")],
                          [sg.Text("Matkul      : Pemrograman Visual 3")]],
                  size=(450,200),
                  font=("Times", 18))
window()
window.close()