# ToDoTemplate
# Список задач

Приложение для управления задачами, использующее FastAPI и PostgreSQL. Приложение позволяет создавать, редактировать, удалять задачи и отслеживать их статус.

## Установка и запуск

1. **Клонируйте репозиторий**:

    ```bash
    git clone git@github.com:OlegKumachev/ToDoTemplate.git
    ```

2. **Настройка базы данных**:

    Создайте `.env` файл в корне проекта и добавьте строки подключения к базе данных:

    ```env
    POSTGRES__USER=your_name_user
    POSTGRES__PASSWORD=your_password
    POSTGRES__DATABASE_NAME=name_database
    POSTGRES__PORT=5432
    ```

3. **Запуск приложения**:
    **Docker**:

    Чтобы запустить приложение с использованием Docker:

    ```bash
    docker compose up --build
    ```

    Приложение будет доступно на порту 8000.

## API

- **POST /**: Создать задачу
  - Тело запроса:
    ```json
    {
      "title": "Заголовок задачи",
      "description": "Описание задачи",
      "due_date": "2025-05-01"
    }
    ```

## Метод URL	Описание
- **GET	/** Получить все задачи
- **GET /{task_id}/**	Получить задачу по ID
- **POST /**	Создать новую задачу
- **PUT /{task_id}/**	Обновить задачу по ID
- **DELETE /{task_id}/** Удалить задачу по ID
