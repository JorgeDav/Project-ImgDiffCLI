pipeline{
	agent {label 'dev'}
	stages {
		stage('Start a Create the virtual environment'){
			steps{
				sh '''
					virtualenv mypython
				'''
			}
		}
		
		stage('Deactivate the virtual environment'){
			steps{
				sh '''
					deactivate
				'''
			}
		
		}
	}
}
