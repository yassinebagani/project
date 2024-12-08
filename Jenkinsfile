pipeline {
    agent any

    environment {
        IMAGE_NAME = "nginx-deployment"
        CONTAINER_NAME = "nginx_deployment"
        DOCKER_NETWORK = "bis_network"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your GitHub repository
                git branch: 'main', url: 'https://github.com/yassinebagani/project.git'
            }
        }

        stage('Prepare Modified Files') {
            steps {
                script {
                    // Create the HTML directory and copy modified files
                    sh '''
                   mkdir -p ./html
cp -r ./html/* ./html/
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the new Nginx image with modified files
                    sh '''
                    docker build -t ${IMAGE_NAME} -f Dockerfile.nginx .
                    '''
                }
            }
        }

        stage('Deploy New Container') {
            steps {
                script {
                    // Stop and remove old container if it exists
                    sh '''
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    '''

                    // Run the new container
                    sh '''
                    docker run -d --name ${CONTAINER_NAME} --network ${DOCKER_NETWORK} -p 8083:80 ${IMAGE_NAME}
                    '''
                }
            }
        }
    }

    post {
        always {
            echo "Deployment completed successfully."
        }
    }
}
