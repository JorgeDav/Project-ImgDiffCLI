pipeline{
	agent {label 'dev'}
	stages {
		stage('Start a Create the virtual environment'){
			steps{
				sh '''
					virtualenv mypython
					source mypython/bin/activate
					deactivate
				'''
			}
		}
		
		stage('Deactivate the virtual environment'){
			steps{
				sh '''
					heo
				'''
			}
		
		}
	}
}
