# QRKot — Кошачий благотворительный фонд

Кроссплатформенный REST API-сервис для сбора пожертвований на проекты помощи котикам. Пользователи могут создавать пожертвования, администраторы — управлять благотворительными проектами. Средства автоматически распределяются между незавершёнными проектами.

## Стек
- Python 3.9+
- FastAPI
- SQLAlchemy (Async)
- fastapi-users (аутентификация JWT)
- Alembic (миграции)
- SQLite
- Pydantic

## Установка
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/khomenkoalx/cat_charity_fund
   cd cat_charity_fund
   ```
2. Создать и активировать виртуальное окружение (пример для Windows Git Bash):
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Настройка окружения
Создайте файл `.env` в корне проекта.
Пример:
```env
# Заголовок приложения и секрет
app_title=Кошачий благотворительный фонд
secret=SUPER_SECRET_KEY

# Подключение к БД (по умолчанию — локальная SQLite)
database_url=sqlite+aiosqlite:///./qrkot.db
```
Примечания:
- Переменные читаются через `app/core/config.py` (pydantic BaseSettings). Если `.env` отсутствует, будут применены значения по умолчанию.

## Миграции (Alembic)
Инициализация уже настроена. Для применения миграций:
```bash
alembic upgrade head
```
Для создания новой миграции (при изменении моделей):
```bash
alembic revision --autogenerate -m "your message"
alembic upgrade head
```

## Запуск приложения
Запуск в dev-режиме (Uvicorn):
```bash
uvicorn app.main:app --reload
```
По умолчанию: `http://127.0.0.1:8000`.

## Документация
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Тесты
Запуск тестов:
```bash
pytest
```

## Postman
Коллекция в `postman_collection/QRKot.postman_collection.json`.
- Перед запуском убедитесь, что сервер поднят.
- При необходимости отредактируйте переменные окружения коллекции.

## Полезное
- Основные роуты подключены в `app/api/routers.py`.
- CRUD-слой — `app/crud/`.
- Валидации проектов — `app/api/validators/charity_project.py`.
- Инвестирование средств — `app/services/investment.py`.

## Автор
- ФИО: Хоменко Александр
- Контакт: https://t.me/drkhomenko
