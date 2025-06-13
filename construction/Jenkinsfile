pipeline {
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

        stage('Install Chrome & Dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y wget curl unzip gnupg

                    # Install Google Chrome
                    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                    apt-get install -y ./google-chrome-stable_current_amd64.deb

                    # Find matching ChromeDriver version
                    CHROME_VERSION=$(google-chrome --version | cut -d ' ' -f 3 | cut -d '.' -f 1)
                    DRIVER_VERSION=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION)
                    wget https://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_linux64.zip
                    unzip chromedriver_linux64.zip
                    mv chromedriver /usr/local/bin/
                    chmod +x /usr/local/bin/chromedriver
                '''
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings'
            }
        }
    }
}
