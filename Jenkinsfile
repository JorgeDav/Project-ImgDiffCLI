pipeline {
        agent any
	triggers { 
		pollSCM('')
 
	}
                stages { 
                        stage('Installing required tools') {
                                steps {
                                        sh 'sudo yum install git -y'
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
					python -m pip install --user virtualenv
					python -m venv mypython
					//source mypython/bin/activate
					python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
					pip install opencv-contrib-python 
					pip install --upgrade scikit-image
					pip install --upgrade imutils
					
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


