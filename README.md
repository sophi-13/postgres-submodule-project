# PostgreSQL Submodule Project

Практическая работа № 1. Система контроля версий Git. Вариант 5:
использование submodules для управления зависимостями проекта.

## Описание

Проект демонстрирует подключение внешней библиотеки для работы с PostgreSQL
с использованием Git Submodules. В `src/db_utils.py` находится функция
`get_connection_params`, формирующая словарь параметров подключения.

## Структура

- `src/` — исходный код проекта;
- `tests/` — модульные тесты;
- `lib/postgresql/` — внешняя библиотека PostgreSQL, подключённая как Git Submodule;
- `docs/` — документация проекта;
- `mkdocs.yml` — конфигурация MkDocs;
- `.github/workflows/` — сценарии GitHub Actions.

## Установка

```bash
git clone --recurse-submodules https://github.com/sophi-13/postgres-submodule-project.git
cd postgres-submodule-project
python -m pip install --upgrade pip
pip install pytest
```

## Тестирование

```bash
python -m pytest -v
```

## Документация

Для локального просмотра установите MkDocs и запустите:

```bash
pip install mkdocs
mkdocs serve
```

Сборка сайта:

```bash
mkdocs build --strict
```

Документация автоматически собирается workflow `Build and Deploy Documentation`
при изменениях в ветках `master`, `development` и `release`. При push в `master`
сайт публикуется в GitHub Pages.

Подробное руководство находится в каталоге [`docs/`](docs/index.md).
