# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt /app/
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Выполняем миграции и собираем статику
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Указываем команду для запуска приложения
CMD ["gunicorn", "weather_project.wsgi:application", "--bind", "0.0.0.0:8000"]

# Открываем порт для веб-сервера
EXPOSE 8000
