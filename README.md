### Древовидное меню Джанго
### Стэк:
- Python 3.9
- Django 4.14
- Postgresql 15.0
## Запустить проект
```
1) Клонировать репозиторий git@github.com:Sapik-pyt/Uptrader.git
```
```
2) py -3.9 -m venv venv - устанавливаем виртуальное окружение , source venv/Scripts/activate  и активируем его
```
```
3) python -m pip install --upgrade pip
```
```
4) pip install -r requirements.txt
```
```
5) Заменить файл env.example на .env и внести все необходимые переменные
```
```
6) python manage.py makemigrations
```
```
7)  python manage.py migrate
```
```
8) python manage.py createsuperuser и создать админа
```
```
9) Заполнить бд. Создать меню с именем "main_menu" и заполнить несколько полей модели Post
```
