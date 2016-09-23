node {

   stage 'Install dependencies'
   checkout scm
   sh './config/jenkins.sh'

   // Test stage
   stage 'Test'
   sh "source .venv/bin/activate && xvfb-run python manage.py test -v 3 -k --parallel 4"

}