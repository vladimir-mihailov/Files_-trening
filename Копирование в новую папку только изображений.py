from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os
import shutil

# Создание окна
window = Tk()
window.withdraw()  # Скрыть основное окно

# Открытие диалогового окна для выбора папки
direct = fd.askdirectory(title="Выбор папки с изображениями")

# Создание папки с суффиксом new
if direct:
    new_dir = os.path.join(direct, "new")  # Правильное создание пути
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

    перемещенные_файлы = []
    ошибки = []

    # Перебор файлов в исходной папке
    for file in os.listdir(direct):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            source_file = os.path.join(direct, file)
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(source_file, destination_file)
                перемещенные_файлы.append(file)
            except Exception as e:
                ошибки.append(f"Ошибка перемещения: {file} код: {e}")

    # Обработка результатов
    if перемещенные_файлы:
        messagebox.showinfo("Успех", f"Файлы перемещены:\n{', '.join(перемещенные_файлы)}")
    else:
        messagebox.showinfo("Информация", "Не найдено изображений для перемещения.")

    if ошибки:
        messagebox.showerror("Ошибки", "\n".join(ошибки))
else:
    messagebox.showwarning("Внимание", "Папка не выбрана.")

window.mainloop()