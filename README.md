# windows

# Создание виртуального окружения
python -m venv .venv

# Активация виртуального окружения
.\.venv\Scripts\Activate.ps1

# Linux / MacOs
python3 -m venv .venv
source ./.venv/bin/activate

# Деактивировать виртуальное окружение
deactivate

# Установка django
pip install django

# Посмотреть установленные пакеты
pip list

# Создание django проекта
django-admin startproject config .

# Установка пакета python-dotenv
pip install python-dotenv

# Установка модуля requests
pip install requests

# Запуск проекта
python manage.py runserver

# Создание приложения
python manage.py startapp assistant_app

# Установка пакетов для RAG
pip install -U langchain langchain-community langchain-openai faiss-cpu langchain-text-splitters

# Установка пакета для работы с переменными окружения
pip install python-dotenv

# Установка пакета для HTTP-запросов
pip install requests

# Применить миграции
python manage.py migrate