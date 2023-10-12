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

image is automatically built and deployed through the Jenkins pipeline.

<br/>

![](https://i.imgur.com/WVvnWzi.png)


# Jenkins Pipeline for Dockerized Django To-Do List Application**

This Jenkins pipeline is designed to automate the continuous integration and deployment process for a Dockerized Django To-Do List application. It consists of various stages that are executed based on specific conditions, primarily targeting the `master` branch. Here's a brief overview of the pipeline:

1. **Agent Configuration**: The pipeline is configured to run on any available Jenkins agent.

2. **Environment Variables**: Several environment variables are defined, including the Docker Hub username, Docker repository name, version part (e.g., Patch, Minor, Major), and an empty TAG variable for Docker image tagging.

3. **Stages**:
   - **Checkout Code**: This stage fetches the source code from a GitHub repository, specific to the `BRANCH_NAME`.

   - **Generate Docker Image Tag**: This stage generates a Docker image tag based on the `BRANCH_NAME` and `VERSION_PART` when the branch is `master`. It executes a shell script and sets the generated tag to the `TAG` environment variable.

   - **Build**: When the branch is `master`, this stage builds a Docker image with the previously generated tag.

   - **Deploy**: Also targeting the `master` branch, this stage pushes the Docker image to the Docker Hub repository using the tag generated earlier.

   - **Environment Cleanup**: This stage cleans up the Docker image with the generated tag after a successful deployment.

4. **Post Actions**: After the pipeline is completed successfully, it prints a success message indicating the successful execution of the pipeline.

This pipeline facilitates the automation of building, tagging, and deploying a Docker image of the Django To-Do List application on the `master` branch. It's a part of a CI/CD process, ensuring that code changes are deployed consistently and reliably.