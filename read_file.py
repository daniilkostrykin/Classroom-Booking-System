import PyPDF2
import re


def clean_schedule_text(text):
    # Исправляем склеенные времена и заголовки
    text = re.sub(r'(\d{2}:\d{2})((?:Лекция|Практическое))', r'\1\n\2', text)

    # Исправляем склеенные дни недели
    text = re.sub(r'([а-яА-Я])(\d{1,2} пара)', r'\1\n\2', text)

    # Исправляем склеенные недели
    text = re.sub(r'(\d{2}:\d{2})(I{1,2} неделя)', r'\1\n\2', text)

    # Добавляем перенос строки перед днями недели
    days = ['Понедельник', 'Вторник', 'Среда',
            'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    for day in days:
        text = text.replace(day, f'\n{day}')

    # Убираем множественные пустые строки
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return text


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()

        # Очищаем и форматируем текст
        text = clean_schedule_text(text)
        return text

    except FileNotFoundError:
        return f"Ошибка: Файл не найден по пути {pdf_path}"
    except Exception as e:
        return f"Произошла ошибка: {e}"


def save_text_to_file(text, output_path):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Текст успешно сохранен в файл {output_path}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


# Основной код
pdf_path = r"C:\Users\Daniil\Downloads\Расписание-аудитории-714933.pdf"
output_path = 'extracted_text.txt'

extracted_text = extract_text_from_pdf(pdf_path)

if "Ошибка" not in extracted_text:
    print("Текст успешно извлечен из PDF")
    save_text_to_file(extracted_text, output_path)
else:
    print(extracted_text)
