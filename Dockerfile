# Используйте официальный образ Python в качестве базового образа
FROM python:3.9

# Установите рабочую директорию контейнера
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade setuptools
RUN chmod 775 . .
# Скопируйте необходимые файлы в контейнер
COPY main.py database.py parser.py /app/
COPY templates /app/templates/


# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Укажите, какой файл нужно запустить при старте контейнера
CMD ["python3", "main.py"]

