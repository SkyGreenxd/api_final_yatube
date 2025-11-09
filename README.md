# Проект Yatube — социальная сеть для авторов

**Yatube** — это учебный проект социальной сети и блог-платформы для авторов и подписчиков, где пользователи могут создавать аккаунты, публиковать записи, комментировать и ставить лайки, а также подписываться на любимых авторов. Платформа поддерживает тематические группы, личные профили, загрузку изображений и удобный просмотр ленты публикаций. Проект реализован на Python с использованием Django и других технологий, включает управление пользователями, страницы ошибок и функции восстановления пароля, что делает его полноценным примером социальной сети для обмена контентом и общения.

---
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке
Cоздать и активировать виртуальное окружение:

Windows
```
python -m venv venv
source venv/Scripts/activate
```
Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Обновить PIP

Windows
```
python -m pip install --upgrade pip
```
Linux/macOS
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

Windows
```
python manage.py makemigrations
python manage.py migrate
```

Linux/macOS
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Запустить проект:

Windows
```
python manage.py runserver
```

Linux/macOS
```
python3 manage.py runserver
```

