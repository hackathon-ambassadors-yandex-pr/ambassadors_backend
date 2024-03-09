## CRM Yandex Ambassadors API

## Оглавление
- [Описание](#описание)
- [Технологии](#технологии)
- [Запуск](#запуск)


## Описание

API CRM системы работы с амбассадорами для Команды реферального маркетинга Яндекс


## Технологии
<details>
<summary>развернуть</summary>

Python 3.11

Django 4.2

Django REST Framework 3.14.0

DRF-Spectacular 0.27.1

Simple JWT 5.3.1

PostgreSQL 16

[⬆️В начало](#оглавление)
</details>


## Запуск
<details>
<summary>локально</summary>

1. Установить сервер баз данных PostgreSQL версии 16 и выше ([документация](https://www.postgresql.org/))

2. Создать базу данных PostgreSQL

3. Создать и активировать виртуальное окружение:
    ```bash
    py -3.11 -m venv venv (Windows)
    python3 -m venv venv (Linux, MacOS)
    
    source venv/Scripts/activate (Windows)
    source venv/bin/activate (Linux, MacOS)
    ```

4. Обновить pip:
    ```bash
    python -m pip install --upgrade pip
    ```

5. Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```

6. Скопировать файл `.env.example` и переименовать в `.env`. 
Установить значения параметров в файле `.env`.

7. Выполнить миграции:
    ```bash
    python manage.py makemigrations
    
    python manage.py migrate
    ```

8. Создать суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

9. Импортировать необходимые для работы данные в БД:
    ```bash
    python manage.py loaddata ../db_data/data.json
    ```

10. Запустить проект:
    ```bash
    python manage.py runserver 8008
    ```

После запуска проект доступен по адресам:
- сайт администратора
    ```markdown
    http://127.0.0.1:8008/admin/
    ```

- статическая документация API
    ```markdown
    http://127.0.0.1:8008/api/redoc/v1/
    
    http://127.0.0.1:8008/api/swagger/v1/
    ```

- динамическая документация API 
(генерируется библиотекой drf-spectacular, доступна при DEBUG=True):
    ```markdown
    http://127.0.0.1:8008/api/dynamic_doc/v1/download/
    
    http://127.0.0.1:8008/api/redoc/v1/dynamic/
    
    http://127.0.0.1:8008/api/swagger/v1/dynamic/
    ```

- CRM Yandex Ambassadors API
    ```markdown
    http://127.0.0.1:8008/api/v1/...
    ```

[⬆️В начало](#оглавление)
</details>