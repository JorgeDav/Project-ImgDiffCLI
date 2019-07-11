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
					sudo cp -R imgdif1-0.2-py3-none-any.whl /home/ec2-user/repo/
					deactivate
					pwd
					sudo cd /
					sudo cd /home/ec2-user/repo/
					sudo scp -r imgdif1-0.2-py3-none-any.whl ec2-user@3.16.49.180:/home/ec2-user/
					sudo cd /
					sudo cd /var/lib/jenkins/workspace/PythonProject
					sudo rm -rf Project-ImgDiffCLI
					sudo cd /
					sudo rm -rf /home/ec2-user/repo/*
				'''
			}
		}
		
                 stage('Deploy'){
                        agent {label 'unit'}
                                steps{
                                        sh '''
						cd /
						cd /home/ec2-user
						pip3 install imgdif1-0.2-py3-none-any.whl --user
						imgapp -f images/image11.png -s images/image1.png
						pip3 uninstall imgdif1-0.2-py3-none-any.whl --user
					'''
                                }
                }
	}

}
