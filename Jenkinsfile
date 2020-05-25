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
        stage('Search node') {
            steps {
                sh  '''
                    node --version
                    npm install -g serverless
                    serverless --version
                '''
            }
        }
    }
}
