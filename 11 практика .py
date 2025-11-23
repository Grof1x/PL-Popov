import tkinter as tk
from tkinter import ttk, messagebox, filedialog


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Попов Илья Романович")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.create_calculator_tab()

        self.create_checkboxes_tab()

        self.create_text_tab()

    def create_calculator_tab(self):
        """Создание вкладки с калькулятором"""
        calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(calc_frame, text="Калькулятор")

        ttk.Label(calc_frame, text="Первое число:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.num1_entry = ttk.Entry(calc_frame)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(calc_frame, text="Второе число:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.num2_entry = ttk.Entry(calc_frame)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(calc_frame, text="Операция:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.operation_var = tk.StringVar()
        operations = ['+', '-', '*', '/']
        self.operation_combo = ttk.Combobox(calc_frame, textvariable=self.operation_var, values=operations,
                                            state='readonly')
        self.operation_combo.set('+')  # значение по умолчанию
        self.operation_combo.grid(row=2, column=1, padx=5, pady=5)

        calc_button = ttk.Button(calc_frame, text="Вычислить", command=self.calculate)
        calc_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        ttk.Label(calc_frame, text="Результат:").grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.result_var = tk.StringVar()
        result_label = ttk.Label(calc_frame, textvariable=self.result_var)
        result_label.grid(row=4, column=1, padx=5, pady=5, sticky='w')

    def calculate(self):
        """Выполнение математической операции"""
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Деление на ноль!")
                result = num1 / num2
            else:
                result = "Неизвестная операция"

            self.result_var.set(str(result))

        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа!")
        except ZeroDivisionError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def create_checkboxes_tab(self):
        """Создание вкладки с чекбоксами"""
        check_frame = ttk.Frame(self.notebook)
        self.notebook.add(check_frame, text="Чекбоксы")

        self.check_var1 = tk.BooleanVar()
        self.check_var2 = tk.BooleanVar()
        self.check_var3 = tk.BooleanVar()

        check1 = ttk.Checkbutton(check_frame, text="Первый", variable=self.check_var1)
        check1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        check2 = ttk.Checkbutton(check_frame, text="Второй", variable=self.check_var2)
        check2.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        check3 = ttk.Checkbutton(check_frame, text="Третий", variable=self.check_var3)
        check3.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        show_button = ttk.Button(check_frame, text="Показать выбор", command=self.show_selection)
        show_button.grid(row=3, column=0, padx=10, pady=20)

    def show_selection(self):
        """Показ выбранных чекбоксов"""
        selected = []

        if self.check_var1.get():
            selected.append("Первый")
        if self.check_var2.get():
            selected.append("Второй")
        if self.check_var3.get():
            selected.append("Третий")

        if selected:
            message = "Вы выбрали: " + ", ".join(selected)
        else:
            message = "Вы ничего не выбрали"

        messagebox.showinfo("Ваш выбор", message)

    def create_text_tab(self):
        """Создание вкладки для работы с текстом"""
        text_frame = ttk.Frame(self.notebook)
        self.notebook.add(text_frame, text="Текст")

        # Создаем меню
        self.create_menu()

        # Текстовое поле
        self.text_widget = tk.Text(text_frame, wrap='word', width=60, height=20)
        self.text_widget.pack(fill='both', expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(text_frame, command=self.text_widget.yview)
        scrollbar.pack(side='right', fill='y')
        self.text_widget.config(yscrollcommand=scrollbar.set)

    def create_menu(self):
        """Создание меню для работы с файлами"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit)

    def open_file(self):
        """Открытие файла и загрузка текста"""
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_widget.delete(1.0, tk.END)
                    self.text_widget.insert(1.0, content)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {str(e)}")


def main():
    root = tk.Tk()
    root.geometry("600x400")
    app = MyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()