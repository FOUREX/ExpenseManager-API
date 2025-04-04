# API Менеджер витрат
- Python 3.13.2 або вище
- Пакетний менеджер [Poetry](https://python-poetry.org/)
- СУБД PostgreSQL


## Запуск проєкту
1. Встановлення необхідних залежностей
```shell
poetry install --no-root
```

2. Запуск віртуального середовища
```shell
poetry env activate
```

3. Створити файл `.env` на основі `.env.template` та заповнити необхідні поля
```
DB_HOST=127.0.0.1
DB_PORT=5432
DB_USER=user
DB_PASS=password
DB_NAME=expensemanager
```

4. Проведення міграцій
```shell
alembic upgrade head
```

5. Запуск проєкту
```shell
uvicorn src.main:app --host 127.0.0.1 --port 25565
```
