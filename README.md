# Оптимизация расписания водителей

Этот проект использует генетический алгоритм для оптимизации расписания водителей. Он включает графический интерфейс для ввода параметров и отображения сгенерированного расписания.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Arturrybkin/-.git
   

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt


## Запуск
Запустите приложение с помощью следующей команды:
    ```bash
    python main.py

# Описание файлов
main.py: Запускает приложение.
gui.py: Создает графический интерфейс.
genetic_algorithm.py: Реализует генетический алгоритм для генерации расписания.
route_generation.py: Генерирует временные интервалы для маршрутов.
schedule_validation.py: Проверяет корректность расписания и вычисляет функцию приспособленности.

### Итоговая структура проекта
├── main.py 
├── gui.py 
├── genetic_algorithm.py 
├── route_generation.py 
├── schedule_validation.py 
├── requirements.txt 
├── .gitignore 
└── README.md

# Описание работы программы
Программа предназначена для оптимизации расписания водителей с использованием генетического алгоритма. Она предоставляет пользователю графический интерфейс для ввода параметров и отображения сгенерированного расписания. Основные функции программы включают:
Генерация временных интервалов маршрутов: Программа создает временные интервалы для маршрутов на основе заданных пиковых и непиковых часов, а также времени, необходимого для прохождения маршрутов с учетом трафика.

Генетический алгоритм: Используется для создания и оптимизации расписания водителей.
Алгоритм инициализирует популяцию случайных расписаний, затем проходит через несколько поколений, отбирая лучшие расписания и создавая новые на основе скрещивания и мутации.

Валидация расписания: Программа проверяет корректность сгенерированного расписания, учитывая правила для разных типов водителей. 
Для водителей типа A проверяется, не превышает ли общее время работы допустимую продолжительность смены, а для водителей типа B — наличие минимального интервала между маршрутами.

Оценка качества расписания: Функция приспособленности вычисляет штрафы за пересечение временных интервалов и проверяет корректность расписания. Чем меньше штрафов, тем лучше качество расписания.

Графический интерфейс: Пользователь может вводить параметры, такие как количество маршрутов, тип водителей и временные интервалы, а затем просматривать сгенерированное расписание в удобном формате.

# Применение
Эта программа может быть полезна для транспортных компаний, которые хотят оптимизировать расписание своих водителей, минимизируя время простоя и улучшая эффективность работы. Она позволяет быстро находить оптимальные решения, адаптируясь к различным условиям и требованиям.