# YaCut
## Проект YaCut — это сервис укорачивания ссылок. 
Заменяет длинную ссылку на короткую
## Возможности сервиса:
- генерация коротких ссылок
- переадресация на исходный адрес при переходе по коротким ссылкам.
## API
API обслуживает два эндпоинта:
- /api/id/ — POST запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone ...
```

```
cd yacut
```

Cоздайте и активируйте виртуальное окружение:

```
python -m venv venv
```

* MacOS/Linux

    ```
    source venv/bin/activate
    ```

*  Windows

    ```
    source venv/scripts/activate
    ```

Установите зависимости:

```
pip install -r requirements.txt
```

Запустите проект:

```
flask run
```

## Технологии:
Flask
Python
REST API
SQLAlchemy
Git

## Автор
Иванов Георгий