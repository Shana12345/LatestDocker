


pipeline {

    agent none



    stages{



            stage('Dependencies'){

                agent {label 'master'}

                steps{

                    sh 'chmod +x ./script/*'

                    sh 'bash ./script/before_installation.sh'

                    sh './script/ansible.sh'

                }

            }



            stage('Deploying Docker Stack'){

                agent {label 'manager_node'}

                steps{

                    sh 'chmod +x ./script/*'

                    sh './script/docker.sh'

                }

            }



    }

}

        stage("Testing"){

            steps{

                sh 'echo "testing db"'
                sh 'chmod 775 ./scripts/*'
                sh 'echo "checking URLs"'
                sh './scripts/tests/testing.py'
                sh './scripts/run_after.sh'

            }

        }

    }

}