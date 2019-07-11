pipeline{
	agent {label 'dev'}
	stages {
//---------SONAR-----------------------------------------
		stage('Open Source Static Code Analysis') {
    			environment {
        		scannerHome = tool 'SonarScan'
    			}
			steps {
        			withSonarQubeEnv('Sonar') {
            			sh "${scannerHome}/bin/sonar-scanner"
        			}
				timeout(time: 10, unit: 'MINUTES') {
            			waitForQualityGate abortPipeline: true
        			}
			}
		}
//-------------------------------------------------------	
		
		 stage('Unit Test'){
        		agent {label 'unit'}
                        	steps{
					sh 'echo "This is our Unit Test" '
				}
		}
		
		stage('Building the App'){
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
					cd dist
					pip install imgdif-0.1-py3-none-any.whl
					imgapp -f ../image1.png -s ../image2.png 
					sudo cp -R imgdif-0.1-py3-none-any.whl /home/ec2-user/repo/
					deactivate
					pwd
					sudo cd /
					pwd
					sudo cd /home/ec2-user/repo
					sudo python3 twine upload -r pypitest imgdif-0.1-py3-none-any.whl
				'''
			}
		}
	}

}
