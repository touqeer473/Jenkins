pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'python -m pytest tests/ -v'  # If you have tests
            }
        }
        
        stage('Deploy to Azure VM') {
            steps {
                sshagent(['azure-deployment-key']) {
                    sh '''
                    scp -o StrictHostKeyChecking=no \
                        *.py requirements.txt \
                        azureuser@<20.17.98.51>:/home/azureuser/app/
                    ssh azureuser@<20.17.98.51> '
                        cd /home/azureuser/app &&
                        pip install -r requirements.txt &&
                        nohup python app.py > app.log 2>&1 &
                    '
                    '''
                }
            }
        }
    }
}