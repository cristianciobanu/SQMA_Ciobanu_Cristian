pipeline {
    agent any
    
    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['test_login', 'test_calculator'],
            description: 'Select which test suite to run'
        )
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Selected Tests') {
            steps {
                sh '''
                    python3 -m pytest ${TEST_SUITE}.py -v --html=report.html --self-contained-html
                '''
            }
        }
    }
    
    post {
        always {
            junit 'test-results.xml' || true
            publishHTML([
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Test Report',
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
