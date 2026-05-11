pipeline{
  agent any

  environment{
    DOCKER_IMAGE = "bhargavalb/my-python-app"
    DOCKER_TAG = "latest"
  }
  stages{
    stage('build'){
      steps{
        sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
      }
    }
    stage('login'){
      steps{
        withCreadentials([usernamePassword(
          creadentialsId:'creadential',
          usernameVariable:'USER',
          passwordVariable:'PASS'
          )]){
          sh 'echo $PASS | docker login -u $USER --password-stdin'
        }
      }
    }
    stage('push'){
      steps{
        sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
      }
    }
    stage('deploy'){
      steps{
        sh '''
        docker stop my-app-container ||true
        docker rm my-app-container ||true
        docker run -d -p 5003:5003 --name my-app-container my-python-app
        '''
      }
    }
  }
}
