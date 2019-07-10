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
					if [[ -d "Project-ImgDiffCLI" ]]; then
						cd Project-ImgDiffCLI
					else
						git clone https://github.com/saulcruzm/Project-ImgDiffCLI
						cd Project-ImgDiffCLI
					fi	
					python3 imgdif/__init__.py -f ../image1.png -s ../image2.png
					python setup.py bdist_wheel 
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
