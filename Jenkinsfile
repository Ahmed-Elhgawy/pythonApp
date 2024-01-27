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
                sh "docker tag python:app elhgawy/python:app${BUILD_ID}"
            }
        }

        stage('push docker image to repo') {
            steps {
                sh "docker push elhgawy/python:app${BUILD_ID}"                
            }
        }

        stage('install application using helm') {
            steps {
                withCredentials([string(credentialsId: 'DB_HOST', variable: 'HOST'), string(credentialsId: 'DB_PASSWD', variable: 'PASSWD')]) {
                    sh "helm install python-app kubernetes/devopsapp --set pod.image=elhgawy/python:app${BUILD_ID} --set DB_HOST=${HOST} --set DB_PASSWD=${PASSWD} -n default"
                }
                
            }
        }
        
    }
}
