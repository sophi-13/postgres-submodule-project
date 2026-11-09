# Установка и запуск

## Требования

- Git;
- Python 3.11;
- pip.

## Клонирование проекта

Для загрузки основного репозитория вместе с внешней библиотекой выполните:

```bash
git clone --recurse-submodules https://github.com/sophi-13/postgres-submodule-project.git
cd postgres-submodule-project
```

Если репозиторий уже был клонирован без подмодулей, инициализируйте их отдельно:

```bash
git submodule update --init --recursive
```

## Установка зависимостей для тестирования

```bash
python -m pip install --upgrade pip
pip install pytest
```

## Запуск тестов

Из корневой директории проекта выполните:

```bash
python -m pytest -v
```

Pytest обнаруживает тесты в каталоге `tests`, что задано в `pytest.ini`.

## Локальный запуск документации

Для предварительного просмотра сайта документации установите MkDocs:

```bash
pip install mkdocs
mkdocs serve
```

После запуска откройте адрес `http://127.0.0.1:8000/`.

Для проверки итоговой сборки без запуска сервера:

```bash
mkdocs build --strict
```

Результат сборки помещается в каталог `site/`.
