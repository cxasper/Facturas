pipeline {
    agent any

    stages {
        stage('Add psycopg2 file at project') {
            steps {
                sh 'pwd'
            }
        }
        stage('Add psycopg2 file at project') {
            steps {
                sh 'ls'
            }
        }
        stage('Remove psycopg2 and psycopg2-binary in requeriments.txt') {
            steps {
                sh 'sed "/django/d" requirements_dev.txt > requirements.txt'
            }
            steps {
                sh 'rm -rf requirements_dev.txt'
            }
        }
    }
}
