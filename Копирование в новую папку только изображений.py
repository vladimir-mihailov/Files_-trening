from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk
import os
import shutil

# Создание окна
window = Tk()
window.title("Перемещение изображений")
window.geometry("300x150")  # Задаем размер окна

# Функция для перемещения изображений
def move_images():
    # Открытие диалогового окна для выбора папки
    direct = fd.askdirectory(title="Выбор папки с изображениями")

    # Создание папки с суффиксом new
    if direct:
        new_dir = os.path.join(direct, "new")  # Правильное создание пути
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        files = [f for f in os.listdir(direct) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        total_files = len(files)  # Общее количество файлов
        перемещенные_файлы = []
        ошибки = []

        # Инициализация прогресс-бара
        progress['maximum'] = total_files
        progress['value'] = 0

        # Перебор файлов в исходной папке
        for index, file in enumerate(files):
            source_file = os.path.join(direct, file)
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(source_file, destination_file)
                перемещенные_файлы.append(file)
            except Exception as e:
                ошибки.append(f"Ошибка перемещения: {file} код: {e}")
            progress['value'] = index + 1  # Обновление значения прогресс-бара
            window.update_idletasks()  # Обновить интерфейс

        # Обработка результатов
        if перемещенные_файлы:
            messagebox.showinfo("Успех", f"Файлы перемещены:\n{', '.join(перемещенные_файлы)}")
        else:
            messagebox.showinfo("Информация", "Не найдено изображений для перемещения.")

        if ошибки:
            messagebox.showerror("Ошибки", "\n".join(ошибки))
    else:
        messagebox.showwarning("Внимание", "Папка не выбрана.")

# Добавление кнопки для запуска функции
btn_move = Button(window, text="Переместить изображения", command=move_images)
btn_move.pack(pady=10)

# Добавление прогресс-бара
progress = ttk.Progressbar(window, length=250)
progress.pack(pady=20)

window.mainloop()