from datetime import datetime, timedelta

def is_time_overlap(start1, end1, start2, end2):
    return max(start1, start2) < min(end1, end2)  # Проверка на пересечение интервалов

def validate_schedule(schedule, driver_type, shift_duration_A):
    """
    Проверяет корректность расписания для водителей.
    
    """
    for routes in schedule.values():  # Проходим по маршрутам каждого водителя
        if driver_type == "A":
            total_time = timedelta()  # Инициализируем общее время как timedelta
            for start, end in routes:
                # Преобразуем время начала и окончания в объекты datetime
                start_time = datetime.combine(datetime.today(), start)
                end_time = datetime.combine(datetime.today(), end)
                total_time += (end_time - start_time)  # Суммируем продолжительность маршрутов

            # Проверяем, не превышает ли общее время допустимое значение
            if total_time > (shift_duration_A - timedelta(hours=1)):
                return False  # Если превышает, возвращаем False
        elif driver_type == "B":
            # Проверяем, что между маршрутами водителей типа B есть минимум 15 минут
            for i in range(1, len(routes)):
                start1 = datetime.combine(datetime.today(), routes[i-1][1])  # Время окончания предыдущего маршрута
                start2 = datetime.combine(datetime.today(), routes[i][0])  # Время начала текущего маршрута
                if (start2 - start1) < timedelta(minutes=15):
                    return False  # Если разница меньше 15 минут, возвращаем False
    return True  # Если все проверки пройдены, возвращаем True

def fitness(schedule, driver_type, shift_duration_A):
    """
    Вычисляет функцию приспособленности для оценки качества расписания.

    """
    # Подсчет штрафов за пересечение временных интервалов
    penalties = sum(
        is_time_overlap(r1[0], r1[1], r2[0], r2[1])
        for routes in schedule.values()
        for i, r1 in enumerate(routes)
        for r2 in routes[i+1:]  # Сравниваем каждый маршрут с последующими
    )
    
    # Проверка корректности расписания и добавление штрафа, если оно некорректно
    if not validate_schedule(schedule, driver_type, shift_duration_A):
        penalties += 10  # Добавляем штраф за некорректное расписание
    
    return -penalties  # Возвращаем отрицательное значение штрафов для минимизации