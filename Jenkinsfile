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
                        steps{
				sh '''
					if [[ -d "Project-ImgDiffCLI" ]]; then
						cd Project-ImgDiffCLI
						git pull
					else
						git clone https://github.com/saulcruzm/Project-ImgDiffCLI
						cd Project-ImgDiffCLI
					fi
					cd imgdif 
					pytest test_funct.py
				'''
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
					mv imgdif/funct.py imgdif/__init__.py
					python setup.py bdist_wheel
					mv imgdif/__init__.py imgdif/funct.py 
					cd dist
					pip install imgdif-0.1-py3-none-any.whl
					imgapp -f ../image1.png -s ../image2.png
					imgapp -f ../image1.png -s ../image11.png 
					sudo cp -R imgdif1-0.2-py3-none-any.whl /home/ec2-user/repo/
					deactivate
					pwd
					sudo cd /
					sudo cd /home/ec2-user/repo/
					sudo scp -r imgdif1-0.2-py3-none-any.whl jenkins@3.16.49.180:/var/lib/jenkins/workspace/PythonProject/
					sudo cd /
					sudo cd /var/lib/jenkins/workspace/PythonProject
					sudo rm -rf Project-ImgDiffCLI
					sudo cd /
					sudo rm -rf /home/ec2-user/repo/*
				'''
			}
		}
		
                 stage('Deploy'){
                        agent {label 'deploy'}
                                steps{
                                        sh '''
						pip3 install imgdif1-0.2-py3-none-any.whl  --user
						imgapp -f image11.png -s image1.png
						pip3 uninstall -y imgdif1-0.2-py3-none-any.whl
					'''
                                }
                }
	}

}
