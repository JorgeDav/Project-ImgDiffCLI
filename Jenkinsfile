pipeline{
	agent {label 'dev'}
	stages {
		stage('Start a Create the virtual environment'){
			steps{
				sh '''
					virtualenv mypython
					source mypython/bin/activate
					pip install numpy --user
					pip install scipy --user
					pip install opencv-contrib-python
					pip install --upgrade scikit-image
					pip install --upgrade imutils
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
