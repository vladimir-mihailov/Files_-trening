from tkinter import *
from tkinter import filedialog as fd
import os

# Создание , скрытие основноего окна
window = Tk()
window.withdraw()

# Открытие диалогового окна для выбора директории
dir = fd.askdirectory(title='Выберите папку с изображеием')

# При открытии директрории выбираем озображения, формат: jpg, jpeg, png.
if dir:
    for file in os.listdir(dir):
        if file.lower().endswith(("jpg","jpeg","png")):
            print(file)

window.mainloop()

