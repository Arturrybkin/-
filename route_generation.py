from datetime import datetime, timedelta 

def generate_route_times(peak_hours, non_peak_hours, traffic_route_time):
   
    route_times = []  # Инициализация списка для хранения временных интервалов
    
    # Объединение пиковых и непиковых часов для обработки
    for hours in peak_hours + non_peak_hours:
        # Преобразование времени начала маршрута в объект datetime
        current_time = datetime.strptime(f"{hours[0]}:00", "%H:%M")
        
        # Цикл для генерации временных интервалов до конца указанного часа
        while current_time.hour != hours[1]:
            route_times.append(current_time.time())  # Добавление текущего времени в список
            current_time += traffic_route_time  # Увеличение текущего времени на время маршрута
    
    return route_times  # Возвращение списка временных интервалов