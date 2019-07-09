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
                                        sh 'python3 get-pip.py --user'
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
                }
}

