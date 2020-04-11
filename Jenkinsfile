pipeline{

    agent any


    stages{

        stage("Test Install"){

            steps{
                sh 'echo "installing docker locally"'
                sh 'chmod 775 ./scripts/*'
                sh './scripts/before_installation.sh'

            }

        }

        stage("Test Docker Swarm"){

            steps{

                sh 'echo "install testing docker-swarm"'
                sh 'chmod 775 ./scripts/*'
                sh './scripts/installation.sh'
                sh '.roles/docker-swarm-init/tasks/main.yml'
                sh 'sudo docker stack deploy --compose-file /var/lib/jenkins/workspace/SaveMe/docker-compose.yml KeepGoing'
                sh 'sleep 10'
                sh 'echo "checking URLs"'
                sh './scripts/tests/testing'
                sh 'sleep 10'

            }

        }

 stage("Installing Ansible"){
            steps{
                sh 'sudo apt update'
                sh 'sudo apt install software-properties-common'
                sh 'sudo apt install ansible'
                sh 'echo "all good to go"'

            }

        }


            stage('Dependencies'){

                agent {label 'master'}

                steps{

                    sh 'chmod +x ./script/*'
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