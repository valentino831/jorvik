node {

   stage 'Install dependencies'
   checkout scm
   sh 'virtualenv --python=python3 .venv'
   sh 'source .venv/bin/activate'
   sh 'pip3 install -r requirements.txt'

   // Test stage
   stage 'Test'
   sh "python manage.py test -v 3 --parallel 2"

}