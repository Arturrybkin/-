import random
from datetime import datetime, timedelta
from schedule_validation import validate_schedule, fitness

def genetic_schedule(driver_list, driver_type, route_times, num_routes, traffic_route_time, shift_duration_A, population_size=100, max_generations=50):
    
    # Инициализация популяции случайных расписаний
    population = [{driver: [] for driver in driver_list} for _ in range(population_size)]
    
    # Заполнение каждого расписания случайными маршрутами
    for schedule in population:
        for _ in range(num_routes):
            driver = random.choice(driver_list)  # Случайный выбор водителя
            start_time = random.choice(route_times)  # Случайный выбор времени начала маршрута
            end_time = calculate_route_end(start_time, traffic_route_time)  # Вычисление времени окончания маршрута
            schedule[driver].append((start_time, end_time))  # Добавление маршрута в расписание

    # Основной цикл генетического алгоритма
    for _ in range(max_generations):
        # Сортировка популяции по функции приспособленности
        population.sort(key=lambda x: fitness(x, driver_type, shift_duration_A), reverse=True)
        
        # Сохранение лучших 10 расписаний для следующего поколения
        next_population = population[:10]
        
        # Генерация новых расписаний до достижения необходимого размера популяции
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)  # Случайный выбор двух родителей из лучших 50
            # Создание потомка, выбирая маршруты от обоих родителей
            child = {driver: random.choice([parent1[driver], parent2[driver]]) for driver in driver_list}
            
            # С вероятностью 20% выполняется мутация
            if random.random() < 0.2:
                driver = random.choice(driver_list)  # Случайный выбор водителя для мутации
                if child[driver]:  # Если у водителя есть маршруты
                    child[driver].pop(random.randint(0, len(child[driver]) - 1))  # Удаление случайного маршрута
                start_time = random.choice(route_times)  # Случайный выбор нового времени начала маршрута
                end_time = calculate_route_end(start_time, traffic_route_time)  # Вычисление времени окончания
                child[driver].append((start_time, end_time))  # Добавление нового маршрута
            
            next_population.append(child)  # Добавление потомка в следующее поколение
        
        population = next_population  # Обновление популяции

    # Возвращение лучшего расписания на основе функции приспособленности
    return max(population, key=lambda x: fitness(x, driver_type, shift_duration_A))

def calculate_route_end(start_time, route_duration):
    return (datetime.combine(datetime.today(), start_time) + route_duration).time()  # Возвращает время окончания