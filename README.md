# API Менеджер витрат
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white&style=flat)](https://www.python.org/downloads/release/python-3132/)
[![Poetry](https://img.shields.io/badge/Poetry-blueviolet?logo=poetry)](https://python-poetry.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue?logo=postgresql&logoColor=white&style=flat)](https://www.postgresql.org/)


## Запуск проєкту
### 1. Встановлення необхідних залежностей
```shell
poetry install --no-root
```

### 2. Запуск віртуального середовища
```shell
poetry env use python3.13
```

Для Windows (якщо результатом виконання команди буде тільки шлях до `.bat` файлу - вставте його в консоль та запустіть):
```shell
poetry env activate
```

Для Linux:
```shell
eval $(poetry env activate)
```

### 3. Створити файл `.env` на основі `.env.template` та заповнити необхідні поля
```
DB_HOST=127.0.0.1
DB_PORT=5432
DB_USER=user
DB_PASS=password
DB_NAME=expensemanager
```

### 4. Проведення міграцій
```shell
alembic upgrade head
```

### 5. Запуск проєкту
```shell
uvicorn src.main:app --host 127.0.0.1 --port 25565
```

### 6. Переходимо за наступним в браузері: http://127.0.0.1:25565/docs
