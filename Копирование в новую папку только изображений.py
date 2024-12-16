from importlib.metadata import files
from tkinter import  *
from tkinter import filedialog as fd
import  os
import shutil

from main import window

#Создание окна и скрытие
window = Tk()
window.withdraw()

# Отерытие диалогового окна для выбора папки
direct = fd.askdirectory(title=" Выбор папки с изображением")

# Создание папки с суфиксом new
if direct:
    new_dir = direct+ "new"
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

        #перебор файлов в исходной папке
        for file in os.listdir(direct):
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                source_file = os.path.join(direct, file)
                destination_file = os.path.join(new_dir, file)
                try:
                    shutil.move(source_file, destination_file)
                    print(f"Файл {file} перемещен")
                except Exception as e:
                    print(f"Ошибка перемещения :{file} код: {e}")

        print(f" Все изображения папки: {direct} перемещены в пакпу: {new_dir}")
else:
    print("Папка не выбрана")

window.mainloop()

