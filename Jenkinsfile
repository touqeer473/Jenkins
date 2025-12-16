pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'echo "Code checked out from GitHub"'
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo "Building application..."'
                sh 'ls -la'
            }
        }
        
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "Deploying to Azure..."'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
        }
    }
}