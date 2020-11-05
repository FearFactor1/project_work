pipeline {
 agent {
  docker {
   image 'API'
  }
 }
 
  stages {
    stage('build') {
      steps {
        sh 'pip install pytest'
      }
    }
    stage('API/test_api.py') {
      steps {
        sh 'python3 -m pytest -v API/test_api.py'
      }   
    }
  }
}
