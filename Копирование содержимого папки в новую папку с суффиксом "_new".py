from tkinter import *
from tkinter import filedialog as fd
import os
import shutil


# Создание и открытие основного окна
window = Tk()
window.withdraw()

#Открытие диалогового окна для выбора папки
dir = fd.askdirectory(title="выбрать папку для копирования")

#Создание новой папки с суфиксом "New"
if dir:
    new_dir = dir+ "new"
    if not os.path.exists(new_dir):
        try:
            shutil.copytree(dir, new_dir)
            print(f"Содержимое папки: {dir} скопировано в :{new_dir}")
        except Exception as e:
            print(f"Ошибка копимровнире с кодом {e}")
    else:
        print(f"Папка {new_dir} уже существует")
else:
    print(f"Папка не выбрана")


window.mainloop()


