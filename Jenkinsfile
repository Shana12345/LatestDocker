
pipeline {
    agent any

    stages{

            stage('Dependencies'){
                agent {label 'master'}
                steps{
                    sh 'chmod +x ./script/*'
                    sh 'bash ./script/before_install.sh'
                    sh './script/ansible.sh'
                }
            }

            stage('Deploying Docker Stack'){
                agent {label 'master'}
                steps{
                    sh 'echo "Beginning deployment"'
                    sh 'chmod +x ./script/*'
                    sh './script/docker-deploy.sh'
                    sh 'echo "Deployment complete!"'
                }
            }
            stage('Testing'){
                steps{
                    sh 'whoami'
                    sh 'sudo chmod -R a+rw ./tests/'


                    sh 'python3 -m pytest ./tests/testing.py'
                    sh 'python3 -m coverage run -m --source=. pytest ./tests/testing.py'
                    sh 'python3 -m coverage report -m ./tests/testing.py'
                    sh 'echo "Testing Successful!"'
                
            }
        }
    }
}