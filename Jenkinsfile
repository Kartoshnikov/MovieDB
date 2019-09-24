pipeline {
    agent { label "QA" }

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
		    steps{
		        sh 'sudo docker-compose exec -T python bash -c "python3 manage.py test core"'
		    }
		}

		stage('Clean up'){
		    when {
		        expression {
		            return true
		        }
		    }
		    steps{
		        sh 'sudo docker-compose down -v'
		    }
		}

		stage('Deploy') {
		    agent { label "PRODUCTION" }
		    steps {
		        sh "sudo docker-compose up --build -d"
		    }
		}

    }
}