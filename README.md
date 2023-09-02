# ToDo List App - Django


## [Live App Link](https://django-todo.astipan.com)

```python
username: test
password: xkLZ79JZAVBBsYu
```



![expected output](https://i.imgur.com/lwSD66R.png)

![expected output](https://i.imgur.com/i4KU4eA.png)

![expected output](https://i.imgur.com/gULqAVW.png)
<br/>

#### For local run:
1. Creat .env and add database credentials
```python
NAME=
USER=
PASSWORD=
HOST=
PORT=
SECRET_KEY=
```
or use default settings

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
2. Make db migration
```cmd
python manage.py migrate
```
3. Run server
```cmd
python manage.py runserver
```
4. Open
```link
http://127.0.0.1:8000/
```
5. or use Docker
```link
docker compose up -d
```

## Admin Django panel
Using admin panel for user and posts management run:

```pyuthon
python manage.py createsuperuser
```

Django [deployment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment) to production environment


