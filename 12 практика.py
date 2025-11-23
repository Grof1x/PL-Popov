import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime


class GitHubRepoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Info")
        self.root.geometry("500x300")

        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(main_frame, text="Получение информации о репозитории GitHub",
                                font=("Arial", 14, "bold"))
        title_label.pack(pady=10)

        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=20)

        ttk.Label(input_frame, text="Имя репозитория:").pack(side=tk.LEFT)
        self.repo_entry = ttk.Entry(input_frame, width=30)
        self.repo_entry.pack(side=tk.LEFT, padx=10)
        self.repo_entry.bind('<Return>', lambda event: self.get_repo_info())

        self.get_button = ttk.Button(main_frame, text="Получить информацию",
                                     command=self.get_repo_info)
        self.get_button.pack(pady=10)

        result_frame = ttk.LabelFrame(main_frame, text="Результат", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.result_text = tk.Text(result_frame, height=8, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(result_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)

        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X, pady=5)

    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip()
        if not repo_name:
            messagebox.showerror("Ошибка", "Введите имя репозитория")
            return

        self.status_var.set("Получение данных...")
        self.get_button.config(state='disabled')
        self.root.update()

        try:
            url = f"https://api.github.com/repos/{repo_name}"

            response = requests.get(url)

            if response.status_code == 200:
                repo_data = response.json()

                owner_data = self.get_owner_info(repo_data['owner']['url'])

                if owner_data:
                    result_data = {
                        'company': owner_data.get('company'),
                        'created_at': owner_data.get('created_at'),
                        'email': owner_data.get('email'),
                        'id': owner_data.get('id'),
                        'name': owner_data.get('name') or owner_data.get('login'),
                        'url': owner_data.get('url')
                    }

                    filename = f"repo_info_{repo_name.replace('/', '_')}.json"
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(result_data, f, ensure_ascii=False, indent=2)

                    self.display_result(result_data, filename)
                    self.status_var.set(f"Данные сохранены в {filename}")

                else:
                    messagebox.showerror("Ошибка", "Не удалось получить информацию о владельце")

            elif response.status_code == 404:
                messagebox.showerror("Ошибка", "Репозиторий не найден")
                self.status_var.set("Репозиторий не найден")
            else:
                messagebox.showerror("Ошибка", f"Ошибка API: {response.status_code}")
                self.status_var.set(f"Ошибка API: {response.status_code}")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка", f"Ошибка сети: {str(e)}")
            self.status_var.set("Ошибка сети")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
            self.status_var.set("Ошибка")
        finally:
            self.get_button.config(state='normal')

    def get_owner_info(self, owner_url):
        """Получает информацию о владельце репозитория"""
        try:
            response = requests.get(owner_url)
            if response.status_code == 200:
                return response.json()
        except:
            pass
        return None

    def display_result(self, data, filename):
        """Отображает результат в текстовом поле"""
        self.result_text.delete(1.0, tk.END)

        display_text = f"Данные сохранены в файл: {filename}\n\n"
        display_text += "Полученная информация:\n"
        display_text += "=" * 50 + "\n"

        for key, value in data.items():
            display_text += f"{key}: {value}\n"

        self.result_text.insert(1.0, display_text)


def main():
    root = tk.Tk()
    app = GitHubRepoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()