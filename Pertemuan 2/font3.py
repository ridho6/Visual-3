import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                  layout=[[sg.Text("SELAMAT DATANG DIKELAS",
                                   font=("Arial", 25, "italic", "bold", "underline"))],
                          [sg.Text("NPM         : 2210010533 ")],
                          [sg.Text("Nama        : Muhammad Ridho Syahputra ")],
                          [sg.Text("Kelas        : 5M Regular Banjarmasin ")],
                          [sg.Text("Matkul      : Pemrograman Visual 3")]],
                  size=(510,200),
                  font=("Times", 18))
window()
window.close()