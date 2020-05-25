pipeline {
    agent any

    tools {nodejs "node v10"}

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
