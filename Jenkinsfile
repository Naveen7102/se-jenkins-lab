pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Naveen7102/se-jenkins-lab.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x power.py"
                sh "./power.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
