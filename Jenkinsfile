pipeline {
        agent any
	triggers { 
		pollSCM('')
 
	}
                stages { 
                        stage('Installing required tools') {
                                steps {
                                        sh 'sudo yum install git -y'
					sh 'sudo yum install python3 -y'
                                        sh 'sudo curl -O https://bootstrap.pypa.io/get-pip.py'
                                        sh 'sudo python3 get-pip.py --user'
					sh 'sudo yum install gcc -y'
                                        sh 'echo "Tools were installed successfully!"'
                                }
                        }

                        stage('Create a local GitHub directory of the repo') {
                                steps {
                                        sh ''' 
					    if [[ -d "GitHub" ]]; then
                                            	cd GitHub
                                            else
                                                mkdir GitHub
                                                cd GitHub
                                            fi
					'''
                                        sh '''
					    if [[ -d "Project-ImgDiffCLI" ]]; then
                                            	cd Project-ImgDiffCLI
                                            else
                                                git clone https://github.com/saulcruzm/Project-ImgDiffCLI
                                                cd Project-ImgDiffCLI
                                            fi
					'''
                                }
                        }
			 
                       stage('Virtual Env') {
                                steps {
				  sh '''
					pip3 install numpy --user
					pip3 install scipy --user
					sudo python3 -m pip install opencv-contrib-python 
					sudo python3 -m pip install --upgrade scikit-image
					sudo python3 -m pip install --upgrade imutils
					
				   '''
                                }
                       }
			 stage('Build') {
                                steps {
                                  sh '''
                                        python3 imgdif/__init__.py -f image1.png -s image11.png
					//deactivate

                                   '''
                                }
                       }

		} 
}       


