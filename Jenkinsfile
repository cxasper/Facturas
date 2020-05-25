pipeline {
    agent any

    stages {
        stage('Add psycopg2 file at project') {
            steps {
                sh 'pwd'
            }
        }
        stage('Add psycoasdapg2 file at project') {
            steps {
                sh 'ls'
            }
        }
        stage('Remove psycopg2 and psycopg2-binary in requeriments.txt') {
            steps {
                sh 'sed "/django/d" requirements_dev.txt > requirements.txt'
            }
        }
        stage('Add psycopg2 asdaasda at project') {
            steps {
                sh 'rm -rf requirements_dev.txt'
            }
        }
    }
}
