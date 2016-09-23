node {

   stage 'Install dependencies'
   checkout scm
   sh './config/jenkins.sh'

   // Test stage
   stage 'Test'
   sh "source .venv/bin/activate && python manage.py test -v 3 --parallel 2"

}