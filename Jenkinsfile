pipeline{
	agent any
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
						git pull
					else
						git clone https://github.com/saulcruzm/Project-ImgDiffCLI
						cd Project-ImgDiffCLI
					fi
					pwd	
					python3 imgdif/__init__.py -f ../image1.png -s ../image2.png
					python setup.py bdist_wheel 
					deactivate
				'''
			}
		}
		/*
		stage('Installing the .whl file locallly'){
			steps{
				sh '''
					cd /home/jenkins/workspace/Project-ImgDiffCLI_master/Project-ImgDiffCLI/dist
					sudo python3 -m pip install imgdif-0.1-py3-none-any.whl
				'''
			}
		
		}

		stage('Verify that the package is installed on the system'){
			steps{
				sh '''
					imgapp -f /home/jenkins/workspace/Project-ImgDiffCLI_master/Project-ImgDiffCLI/image1.png -s /home/jenkins/workspace/Project-ImgDiffCLI_master/Project-ImgDiffCLI/image2.png
				'''
			}
		}
		*/
		stage('Sonarqube') {
    			environment {
        		scannerHome = tool 'SonarScanner'
    			}
			steps {
        			withSonarQubeEnv('Sonar') {
            			sh "sh {scannerHome}/bin/sonar-scanner"
        			}
				timeout(time: 10, unit: 'MINUTES') {
            			waitForQualityGate abortPipeline: true
        			}
			}
		}
	
	}
}
