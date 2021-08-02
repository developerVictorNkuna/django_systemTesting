created django new project deffault file,

create test setting file,putting next to original settinggs file
a  name with allowed arguments
Iamgine  a model function that returns truncated body,gives short version of the body
Create our own api before even test_settings
g

Always return a message  and body of the obj = mixer.blend(Data,body='',message='')



TESING VIEWS IN DJANGO_SETTINGS_MODULE

-We want to create a view that can be seen by anyone
-Django's "self.client.get()" is slow



Before you implement the function ,you have to write test
That means you have to you 'use' your fucntion nefore it exists
This helps me as tester to think deeply about it,came up with 



in-memory db is very fast,
pytest-pdb,alls us to add break points 
install pytest-pdb
pytest-cov generates reports for us,aim for 100% test coverage.small situation test coverage goes down.

create pytest.ini in the root of the django project

for configuring pytest to generate html reports

pytest is like nose,search recursively to find your test


cov,everytime I run my tests
even pdf

DJANGO_SETTINGS_MODULE=projectname.test_settings
addpots = --nomigrations --cov=. --cov=report=html,pdf,word,any forma,json


add more options to cmd argv
add-options=addopts

django-discover-runner locate tests if if organized outside the test.py file

# djangoSystemTesting
# djangoSystemTesting
# djangoSystemTesting
# django_systemTesting
# django_systemTesting
# django_systemTesting
# django_systemTesting
