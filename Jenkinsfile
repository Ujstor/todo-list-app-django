pipeline {
  agent any

  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/Ujstor/todo-list-app-django/', branch: 'master')
      }
    }

    stage('Build') {
      steps {
        script {
          sh 'docker build -t ujstor/django_todolist .'
        }
      }
    }

    stage('Deploy') {
      steps {
        script {
          sh 'docker push ujstor/django_todolist'
        }
      }
    }
  }
}