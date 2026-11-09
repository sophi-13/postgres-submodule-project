# Структура проекта

Основные элементы репозитория:

| Путь | Назначение |
|---|---|
| `src/` | Исходный код проекта |
| `src/db_utils.py` | Функция формирования параметров подключения к БД |
| `tests/` | Модульные тесты |
| `tests/test_db_utils.py` | Проверки функции `get_connection_params` |
| `lib/postgresql/` | Внешняя библиотека, подключённая как Git Submodule |
| `.gitmodules` | URL и путь подключённого подмодуля |
| `.github/workflows/` | Сценарии автоматизации GitHub Actions |
| `pytest.ini` | Настройки обнаружения тестов pytest |
| `docs/` | Исходные Markdown-файлы документации |
| `mkdocs.yml` | Конфигурация сайта документации MkDocs |

## Исходная функция

Модуль `src/db_utils.py` содержит функцию `get_connection_params`.
Она возвращает словарь с ключами `dbname`, `user`, `password`, `host` и `port`.
Параметры `host` и `port` имеют значения по умолчанию `localhost` и `5432`.
