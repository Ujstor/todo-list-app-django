pipeline {
    agent any

    environment {
        DOCKER_HUB_USERNAME = 'ujstor'
        DOCKER_REPO_NAME = 'django_todolist'
        VERSION_PART = 'Patch' // Patch, Minor, Major
        TAG = ''
    } 

    stages {
        stage('Checkout Code') {
            steps {
                git(url: 'https://github.com/Ujstor/todo-list-app-django/', branch: env.BRANCH_NAME)
            }
        }


        stage('Generate Docker Image Tag') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                script {
                    TAG = sh(script: "/var/lib/jenkins/scripts/docker_tag.sh $DOCKER_HUB_USERNAME $DOCKER_REPO_NAME $VERSION_PART", returnStdout: true).trim()

                    if (TAG) {
                        echo "Docker image tag generated successfully: $TAG"
                    } else {
                        error "Failed to generate Docker image tag"
                    }

                    env.TAG = TAG
                }
            }
        }

        stage('Build') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                script {
                    sh "docker build --no-cache -t ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG} ."
                }
            }
        }

        stage('Deploy') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                script {
                    sh "docker push ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG}"
                }
            }
        }

        stage('Environment Cleanup') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                script {
                    sh "docker rmi ${DOCKER_HUB_USERNAME}/${DOCKER_REPO_NAME}:${TAG}"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully"
        }
    }
}