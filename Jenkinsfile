pipeline{
	agent {label 'dev'}
	stages {
		stage('Install Python & Pip'){
			steps{
				sh '''
					sudo yum install python3
					python3 get-pip.py
				'''
			}
		}
		
		stage('Install virtualenv'){
			steps{
				sh '''
					sudo python3 get-pip.py --user
				'''
			}
		
		}
	}
}
