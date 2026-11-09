# API

## `get_connection_params`

Модуль: `src/db_utils.py`

```python
def get_connection_params(database, user, password, host="localhost", port=5432):
    return {
        "dbname": database,
        "user": user,
        "password": password,
        "host": host,
        "port": port
    }
```

### Параметры

| Параметр | Описание |
|---|---|
| `database` | Имя базы данных |
| `user` | Имя пользователя PostgreSQL |
| `password` | Пароль пользователя |
| `host` | Адрес сервера; по умолчанию `localhost` |
| `port` | Порт сервера; по умолчанию `5432` |

### Возвращаемое значение

Функция возвращает словарь параметров подключения со следующими ключами:
`dbname`, `user`, `password`, `host`, `port`.

### Пример

```python
from src.db_utils import get_connection_params

params = get_connection_params(
    "my_database",
    "postgres",
    "my_password",
    host="127.0.0.1",
    port=5433
)

print(params)
```

Функция только формирует словарь параметров. Она сама не устанавливает соединение
с сервером PostgreSQL.
