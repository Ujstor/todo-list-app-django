# ToDo List App - Django


## [Live App Link](https://todolist-app-django-production.up.railway.app/)

<pre>
username: test
password: xkLZ79JZAVBBsYu
</pre>



![expected output](https://i.imgur.com/lwSD66R.png)

![expected output](https://i.imgur.com/i4KU4eA.png)

![expected output](https://i.imgur.com/gULqAVW.png)
<br/>

#### For local run: 
1. Modify settings.py and add database credentials or use sqlite3
```python
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
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

Django [deployment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment) to production environment


