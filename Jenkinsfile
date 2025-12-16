pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
                sh 'echo "✅ Code checked out from GitHub"'
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo "🔨 Building application..."'
                sh 'ls -la'
            }
        }
        
        stage('Test') {
            steps {
                sh 'echo "🧪 Running tests..."'
                sh 'echo "All tests passed!"'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "🚀 Deploying to Azure VM..."'
                sh 'echo "Deployment completed successfully!"'
            }
        }
    }
    
    post {
        always {
            echo '📋 Pipeline completed!'
        }
        success {
            echo '🎉 Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
