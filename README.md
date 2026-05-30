# 🤖 Нейросотрудник — веб-приложение с GPT и базой знаний

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://djangoproject.com)
[![LangChain](https://img.shields.io/badge/LangChain-1.2-orange.svg)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-purple.svg)](https://openai.com)
[![FAISS](https://img.shields.io/badge/FAISS-векторный%20поиск-red.svg)](https://github.com/facebookresearch/faiss)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **AI-ассистент для бизнеса**, который отвечает на вопросы клиентов и сотрудников строго по вашим документам — инструкциям, регламентам, прайсам, FAQ. Работает 24/7, не галлюцинирует, не выходит за рамки базы знаний.

---

## 🎯 Для кого этот проект

| Задача бизнеса | Что делает нейросотрудник |
|---|---|
| Служба поддержки отвечает одно и то же 100 раз в день | Бот отвечает вместо оператора по вашим FAQ и скриптам |
| Новые сотрудники долго изучают регламенты | Бот мгновенно отвечает на вопросы по внутренним документам |
| Клиенты не находят нужное на сайте | Умный поиск по базе знаний прямо в чате |
| HR перегружен одинаковыми вопросами | Бот-ассистент по кадровым документам и политикам |

---

## ✨ Что умеет

- 💬 **Диалог на естественном языке** — клиент пишет как обычно, бот понимает смысл
- 📚 **RAG-архитектура** — ответы только по вашим документам, никакой «отсебятины»
- 🔍 **Семантический поиск** по базе знаний (FAISS + embeddings)
- 🌐 **Веб-интерфейс** — работает в браузере, не нужно ничего устанавливать
- 🔒 **Безопасность** — API-ключи в переменных окружения, не попадают в код
- ⚡ **Быстрый старт** — загрузите свои документы, и бот готов к работе

---

## 🏗️ Архитектура

```
┌─────────────────────────────────────────────────┐
│                  Веб-интерфейс (Django)          │
└─────────────────────┬───────────────────────────┘
                      │ запрос пользователя
┌─────────────────────▼───────────────────────────┐
│              assistant_core (LangChain)          │
│  ┌──────────────┐    ┌──────────────────────┐   │
│  │   FAISS      │    │   OpenAI GPT-4       │   │
│  │ векторная БД │◄───│   (генерация ответа) │   │
│  │ (документы)  │    └──────────────────────┘   │
│  └──────────────┘                               │
└─────────────────────────────────────────────────┘
```

**Стек технологий:**
- **Backend:** Django 6.0, SQLAlchemy, Alembic
- **AI / RAG:** LangChain 1.2, LangGraph, OpenAI GPT-4, FAISS
- **Embeddings:** langchain-openai (text-embedding-3-small)
- **База данных:** SQLite (легко заменяется на PostgreSQL)

---

## 🚀 Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/mantonkov-ux/neuro_employee_code-HW-Pro.git
cd neuro_employee_code-HW-Pro
```

### 2. Создать и активировать виртуальное окружение

```bash
# Windows
python -m venv .venv
.venv\Scripts\Activate.ps1

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Настроить переменные окружения

Скопируйте `.env.example` в `.env` и заполните:

```env
OPENAI_API_KEY=ваш_ключ_openai
```

### 5. Применить миграции и запустить

```bash
python manage.py migrate
python manage.py runserver
```

Откройте браузер: **http://127.0.0.1:8000**

---

## 📁 Структура проекта

```
neuro_employee_code-HW-Pro/
├── assistant_app/        # Django-приложение (views, urls, models)
├── assistant_core/       # Ядро RAG: загрузка документов, FAISS, LangChain
├── config/               # Настройки Django
├── .env.example          # Шаблон переменных окружения
├── manage.py
└── requirements.txt
```

---

## 🔧 Как добавить свою базу знаний

1. Поместите документы (`.txt`, `.pdf`, `.docx`) в папку `assistant_core/knowledge/`
2. Запустите индексацию:
   ```bash
   python manage.py index_documents
   ```
3. Бот готов отвечать по вашим материалам

---

## 💼 Заказать под свой бизнес

Этот проект является демонстрацией навыков. Я разрабатываю подобные решения на заказ:

- 🎯 Нейроконсультант под ваш бизнес (магазин, клиника, юридическая фирма и др.)
- 📦 Интеграция с Telegram, WhatsApp, вашим сайтом
- 🗄️ Подключение к вашим документам и CRM
- ⚙️ Настройка под конкретный сценарий (поддержка, продажи, HR, обучение)

**📩 Написать мне:** [Kwork-профиль](https://kwork.ru/user/mantonkov) | [GitHub](https://github.com/mantonkov-ux)

---

## 📄 Лицензия

MIT — используйте свободно в своих проектах.

---

*Проект разработан в рамках обучения в [Университете Искусственного Интеллекта](https://university.ai) (Москва) по специальности GPT Engineer.*
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
