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
                        azureuser@<deployment-vm-ip>:/home/azureuser/app/
                    ssh azureuser@<deployment-vm-ip> '
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
