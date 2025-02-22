import re

def filter_by_dictionary(input_file, output_file):
    # Словарь с допустимыми значениями
    allowed_values = {
        "пары": [f"{i} пара" for i in range(1, 9)],  # 1-8 пара
        "недели": ["I неделя", "II неделя", "I-II неделя"],  # I, II, I-II неделя
        "дни_недели": ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"],
        "время": [
            "08:00 - 09:30", "09:40 - 11:10", "11:20 - 12:50",
            "13:20 - 14:50", "15:00 - 16:30", "16:40 - 18:10",
            "18:20 - 19:50", "20:00 - 21:30"
        ]
    }

    # Открываем исходный файл для чтения
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Открываем выходной файл для записи
    with open(output_file, 'w', encoding='utf-8') as out:
        for line in lines:
            line = line.strip()
            
            # Проверяем, является ли строка днём недели
            if line in allowed_values["дни_недели"]:
                out.write(line + '\n')
                continue
            
            # Проверяем, является ли строка номером пары
            if line in allowed_values["пары"]:
                out.write(line + '\n')
                continue
            
            # Проверяем, является ли строка временем
            if line in allowed_values["время"]:
                out.write(line + '\n')
                continue
            
            # Проверяем, является ли строка информацией о неделе
            if line in allowed_values["недели"]:
                out.write(line + '\n')
                continue

# Укажите пути к вашим файлам
input_file = 'extracted_text.txt'  # Путь к исходному файлу
output_file = 'formatted_schedule.txt'  # Путь к выходному файлу

# Запускаем функцию для фильтрации расписания
filter_by_dictionary(input_file, output_file)

print("Файл успешно отфильтрован!")