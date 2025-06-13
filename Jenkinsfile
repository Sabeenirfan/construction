pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Sabeenirfan/construction.git'
            }
        }

        stage('Test Inside Docker') {
            steps {
                sh '''
                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.12 bash -c "
                            apt-get update && \
                            apt-get install -y chromium-driver && \
                            pip install -r requirement.txt && \
                            pytest --maxfail=1 --disable-warnings
                        "
                '''
            }
        }
    }
}
