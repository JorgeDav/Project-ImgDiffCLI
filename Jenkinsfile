pipeline{
	agent {label 'dev'}
	stages {
		stage('Start a Create the virtual environment'){
			steps{
				sh '''
					virtualenv mypython
					source mypython/bin/activate
					pip install numpy 
					pip install scipy 
					pip install opencv-contrib-python
					pip install scikit-image
					pip install imutils
					pip install wheel
					pip install twine
					deactivate
				'''
			}
		}
		
		stage('Deactivate the virtual environment'){
			steps{
				sh '''
					
				'''
			}
		
		}
	}
}
