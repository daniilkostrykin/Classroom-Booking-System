import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)  # PdfReader вместо PdfFileReader

            for page_num in range(len(reader.pages)): # reader.numPages заменено на len(reader.pages)
                page = reader.pages[page_num] # getPage заменено на pages[page_num]
                text += page.extract_text()

        return text

    except FileNotFoundError:
        return f"Ошибка: Файл не найден по пути {pdf_path}"
    except Exception as e:
        return f"Произошла ошибка: {e}"


pdf_path = r"C:\Users\Daniil\Downloads\Расписание-аудитории-714933.pdf"
extracted_text = extract_text_from_pdf(pdf_path)

if "Ошибка" not in extracted_text:  # Проверка на наличие ошибки в возвращенном тексте
    print(extracted_text)
    # Сохранение в файл (опционально)
    with open('extracted_text.txt', 'w', encoding='utf-8') as f:
        f.write(extracted_text)
    print("Текст сохранен в файл extracted_text.txt")
else:
    print(extracted_text)  # Вывод сообщения об ошибке