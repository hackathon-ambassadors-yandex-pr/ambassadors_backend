## CRM Yandex Ambassadors API

## Оглавление
- [Описание](#описание)
- [Технологии](#технологии)
- [Запуск](#запуск)
- [CI/CD](#cicd)


## Описание

API CRM системы работы с амбассадорами для Команды реферального маркетинга Яндекс


## Технологии
<details>
<summary>развернуть</summary>

[Python 3.11](https://www.python.org/downloads/release/python-3110/)

[Django 4.2](https://docs.djangoproject.com/en/4.2/releases/4.2/)

[Django REST Framework 3.14.0](https://www.django-rest-framework.org/)

[DRF-Spectacular 0.27.1](https://drf-spectacular.readthedocs.io/en/latest/#)

[Simple JWT 5.3.1](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/#)

[PostgreSQL 16](https://www.postgresql.org/docs/16/index.html)

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

6. Скопировать файл `.env.example_local` и переименовать в `.env`. 
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

9. Импортировать в БД необходимые для работы данные:
    ```bash
    python manage.py loaddata ../db_data/data.json
    ```

10. При необходимости импортировать в БД тестовые данные:
    ```bash
    python manage.py loaddata ../db_data/test_data.json
    ```
    а также создать папку `backend/media/` и скопировать в неё содержимое папки `db_data/test_media/`

11. Запустить проект:
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


<details>
<summary>на удалённом сервере</summary>

1. Скопировать на сервер следующие файлы:
    ```shell
    scp -r <path_to_folder>/compose_files <username>@<server_pub_ip>:/<path_to_folder>/ambassadors
    scp <path_to_file>/nginx.conf <username>@<server_pub_ip>:/<path_to_folder>/ambassadors
    scp <path_to_file>/.env.example_remote_prod <username>@<server_pub_ip>:/<path_to_folder>/ambassadors
    ```

2. Подключиться к серверу
    ```shell
    ssh <username>@<server_ip>
    ```

3. Переименовать файл `.env.example_remote_prod` в `.env`
    ```shell
    mv <path_to_file>/.env.example_remote_prod <path_to_file>/.env
    ```

4. Открыть файл `.env` и задать значения параметров
    ```shell
    nano <path_to_file>/.env
    ```

5. Установить [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
и [плагин Compose](https://docs.docker.com/compose/install/linux/#install-the-plugin-manually).
Выполнить [действия после установки Linux для Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/).

6. Перейти в папку `ambassadors/compose_files/`
    ```shell
    cd <path_to_folder>/ambassadors/compose_files
    ```

7. Выполнить
   - для запуска сервера с тестовыми данными в БД:
      ```shell
      docker compose -f docker-compose.dev.yml up -d
      ```

   - для запуска сервера без тестовых данных в БД:
      ```shell
      docker compose -f docker-compose.prod.yml up -d
      ```

После запуска проект доступен по адресам:
- сайт администратора (данные суперпользователя согласно соответствующим значениям в файле `.env`)
    ```markdown
    http://<server_ip>/admin
    ```

- Интерактивная документация API:
    ```markdown
    http://<server_ip>/api/redoc/v1/
    
    http://<server_ip>/api/swagger/v1/
    ```

- CRM Yandex Ambassadors API
    ```markdown
    http://<server_ip>/api/v1/...
    ```

[⬆️В начало](#оглавление)
</details>

## CI/CD
<details>
<summary>описание и настройка</summary>

- при пуше в любую Git ветку запускаются тесты
- при мёрдже PR в ветки `develop` или `release/` проект запускается на удалённом сервере
с импортированными в БД необходимыми для работы данными и тестовыми данными
- при мёрдже PR в ветку `main` проект запускается на удалённом сервере
с импортированными в БД необходимыми для работы данными

Для корректной работы CI/CD необходимо создать секретные переменные репозитория 
(Repository secrets):
```text
DOCKER_USERNAME=<docker_username>
DOCKER_PASSWORD=<docker_password>

SERVER_HOST=<server_pub_ip>
SERVER_USER=<username>

SSH_KEY=<--BEGIN OPENSSH PRIVATE KEY--...--END OPENSSH PRIVATE KEY--> # cat ~/.ssh/id_rsa
```

[⬆️В начало](#оглавление)
</details>
