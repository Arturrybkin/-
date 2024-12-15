import tkinter as tk
from tkinter import ttk
from genetic_algorithm import genetic_schedule
from route_generation import generate_route_times
from datetime import timedelta

# Определение глобальных переменных
peak_hours = [(7, 9), (17, 19)]
non_peak_hours = [(6, 7), (9, 17), (19, 3)]
traffic_route_time = timedelta(minutes=70)
drivers_A = ["Driver_A1", "Driver_A2", "Driver_A3"]
drivers_B = ["Driver_B1", "Driver_B2"]
shift_duration_A = timedelta(hours=8)

def generate_schedule(driver_type, drivers, num_routes, route_times, tree):
    try:
        if not drivers:
            for i in tree.get_children():
                tree.delete(i)
            tree.insert("", "end", values=(f"Нет водителей типа {driver_type}.", "", ""))
            return
        best_schedule = genetic_schedule(drivers, driver_type, route_times, num_routes, traffic_route_time, shift_duration_A)
        display_schedule(best_schedule, tree)
    except ValueError:
        for i in tree.get_children():
            tree.delete(i)
        tree.insert("", "end", values=("Ошибка: Введите корректные параметры.", "", ""))

def display_schedule(schedule, tree):
    
    for i in tree.get_children():
        tree.delete(i)  # Очистка существующих строк
    for driver, routes in schedule.items():
        for start, end in routes:
            tree.insert("", "end", values=(driver, start.strftime('%H:%M'), end.strftime('%H:%M')))

def create_gui():
    
    root = tk.Tk()
    root.title("Оптимальное расписание")
    root.geometry("600x400")
    root.configure(bg="#2E2E2E")

    # Конфигурация стиля
    style = ttk.Style()
    style.configure("TButton", background="#4CAF50", foreground="black", font=("Helvetica", 12))
    style.configure("TEntry", font=("Helvetica", 12))
    style.configure("Treeview", font=("Helvetica", 12), background="#FFFFFF", foreground="#000000")
    style.configure("Treeview.Heading", font=("Helvetica", 12, 'bold'))

    # Метка для ввода количества маршрутов
    num_routes_label = tk.Label(root, text="Количество маршрутов:", bg="#2E2E2E", fg="red", font=("Helvetica", 12))
    num_routes_label.pack(pady=5)
    
    num_routes_entry = ttk.Entry(root, width=10)
    num_routes_entry.insert(0, "10")
    num_routes_entry.pack(pady=5)

    # Создание Treeview для отображения расписания
    columns = ("Driver", "Start Time", "End Time")
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading("Driver", text="Водитель")
    tree.heading("Start Time", text="Время начала")
    tree.heading("End Time", text="Время окончания")
    tree.pack(pady=10, fill=tk.BOTH, expand=True)

    # Генерация времени маршрутов
    route_times = generate_route_times(peak_hours, non_peak_hours, traffic_route_time)

    # Информационная метка
    info_label = tk.Label(root, text="Нажмите кнопку для генерации расписания для выбранного типа водителей.", bg="#2E2E2E", fg="white", font=("Helvetica", 10))
    info_label.pack(pady=5)

    # Кнопки для генерации расписаний
    button_frame = tk.Frame(root, bg="#2E2E2E")
    button_frame.pack(pady=5)

    type_a_button = ttk.Button(button_frame, text="Генерировать для Тип A", command=lambda: generate_schedule("A", drivers_A, int(num_routes_entry.get()), route_times, tree))
    type_a_button.pack(side=tk.LEFT, padx=10)

    type_b_button = ttk.Button(button_frame, text="Генерировать для Тип B", command=lambda: generate_schedule("B", drivers_B, int(num_routes_entry.get()), route_times, tree))
    type_b_button.pack(side=tk.LEFT, padx=10)

    # Кнопка выхода
    exit_button = ttk.Button(root, text="Выход", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()