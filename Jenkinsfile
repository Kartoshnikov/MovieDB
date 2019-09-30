pipeline {
    agent { label "QA" }
    triggers { githubPush() }
	options {
		buildDiscarder(logRotator(daysToKeepStr: '2', numToKeepStr: '4'))
		timeout( time: 10, unit: 'MINUTES' )
		timestamps()
	}

	stages {
        stage('Git clone'){
			steps {
                git url: 'git@github.com:Kartoshnikov/MovieDB.git', branch: 'master', credentialsId: 'GitHub'
            }
		}

		stage('Build'){
		    steps{
		        sh "sudo docker-compose up --build -d"
		    }
		}

		stage('Test'){
            options {
                timeout(time: 120, unit: 'SECONDS')
            }
		    steps {
				script {
					waitUntil {
						def res = sh script: 'sudo docker-compose exec -T python bash -c "python3 manage.py test core"', returnStatus: true
						return (res == 0)
					}
				}
		    }
		    post {
                always {
                    sh 'sudo docker-compose down -v'
                }
		    }
		}

		stage('Deploy') {
		    agent { label "PRODUCTION" }
		    steps {
		        sh "sudo docker-compose up --build -d"
		    }
		}
    }

    post {
        always {
            deleteDir()
        }
    }
}