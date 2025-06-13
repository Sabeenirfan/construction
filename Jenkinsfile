pipeline {
    agent any

    stages {
        stage('Run in Docker') {
            agent {
                docker {
                    image 'python:3.12'
                }
            }
            stages {
                stage('Clone') {
                    steps {
                        git 'https://github.com/Sabeenirfan/construction.git'
                    }
                }

                stage('Install dependencies') {
                    steps {
                        sh 'apt-get update'
                        sh 'apt-get install -y chromium-driver'
                        sh 'pip install -r requirement.txt'
                    }
                }

                stage('Run Tests') {
                    steps {
                        sh 'pytest --maxfail=1 --disable-warnings'
                    }
                }
            }
        }
    }
}
