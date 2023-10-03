# ToDo List App - Django


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
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
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

## Admin Django panel
Using admin panel for user and posts management run inside app container:

```pyuthon
python manage.py createsuperuser
```

Django [deployment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment) to production environment

## Docker

To build the Docker image from the code, run:

```
docker compose -f .\docker-compose-dev.yml up
```

If you want to pull the image from the Docker repository instead, use:

```
docker compose -f .\docker-compose-prod.yml up
```

Iimage is automatically built and deployed through the Jenkins pipeline, so you may not need to manually run these commands in most cases.

<br/>

![]()


