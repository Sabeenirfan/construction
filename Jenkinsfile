pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Sabeenirfan/construction.git'
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
                            apt-get install -y chromium chromium-driver && \
                            pip install -r requirement.txt && \
                            pytest --maxfail=1 --disable-warnings -v
                        "
                '''
            }
        }
    }
    post {
        always {
            // Clean up any dangling containers
            sh 'docker system prune -f || true'
        }
        failure {
            echo 'Pipeline failed. Check the logs above for details.'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
    }
}
