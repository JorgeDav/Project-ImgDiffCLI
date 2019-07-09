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
			 
                       stage('Install Dependencies') {
                                steps {
				  sh '''
					sudo pip install numpy --user
					sudo pip install scipy --user
					sudo python3 -m pip install opencv-contrib-python 
					sudo python3 -m pip install --upgrade scikit-image
					sudo python3 -m pip install --upgrade imutils
					sudo yum install libXext libSM libXrender -y
					sudo pip3 install wheel
					sudo pip3 install twine
					
				   '''
                                }
                       }
			 stage('Build') {
                                steps {
                                  sh '''
					pwd
					tree
                                        python3 setup.py bdist_wheel
					cd dist
					sudo pip3 install imgdif-0.1-py3-none-any.whl
					cd ..
					imgapp -f image1.png -s image2.png
                                   '''
                                }
                       }

		} 
}       


