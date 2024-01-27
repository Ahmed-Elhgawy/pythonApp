pipeline {
    agent {label "docker-agant"} 

    stages{
       stage('login to docker repo') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Docker', passwordVariable: 'PASSWD', usernameVariable: 'USER')]) {
                    sh "docker login -u ${USER} -p ${PASSWD}"
                }               
            }
        }

       stage('build docker image') {
            steps {
                sh "docker build . -t python:app"
                sh "docker tag node:app elhgawy/python:app${BUILD_ID}"
                sh "docker push elhgawy/python:app${BUILD_ID}"                
            }
        }

        stage('push docker image to repo') {
            steps {
                sh "docker push elhgawy/python:app${BUILD_ID}"                
            }
        }

        stage('install application using helm') {
            steps {
                withCredentials([string(credentialsId: 'DB_HOST', variable: 'DB_HOST'), string(credentialsId: 'DB_PASSWD', variable: 'DB_PASSWD')]) {
                    sh "helm install python-app kubernetes/devopsapp --set pod.image=elhgawy/python:app${BUILD_ID} --set DB_HOST=${DB_HOST} --set DB_PASSWD=${DB_PASSWD}"
                }
                
            }
        }
        
    }
}
