  
pipeline {
    agent none

    stages{

            stage('Dependencies'){
                agent {label 'master'}
                steps{
                    sh 'chmod +x ./scripts/*'
                    sh 'sudo bash ./scripts/before_installation.sh'
                    sh './scripts/ansible.sh'
                }
            }

            stage('Deploying Docker Stack'){
                agent {label 'manager_node'}
                steps{
                    sh 'chmod +x ./scripts/*'
                    sh './script/docker.sh'
                }
            }

    }
}