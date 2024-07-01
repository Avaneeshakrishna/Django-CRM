# A simple Customer Relationship Management site using Django

Customer relationship management is a process in which a business or other organization administers its interactions with customers, typically using data analysis to study large amounts of information


## Getting Started
* Open GitBash
  
  	* mkdir /G/FSU/DjCRM
	* cd /G/FSU/DjCRM


* Create Virtual Environment
  
  	* python -m venv virt

* Activate virt
  
  	* source virt/Scripts/activate

### Dependencies

* Install Django
  
  	* pip install Django

* Install MySQL

  	* pip install MySQL

* Install connectors to connect between MySQL and Django

	* pip install mysql-connector-python
	* pip install mysql-connector

Note: I got error while connecting to database, SO I had to uninstall both and install only mysql-connector-python

* Install MySQL server community edition

* Create Django project

  	* django-admin startproject dcrm  -> create a directory called dcrm

* cd dcrm/

	* This dir contains manage.py

* Now we need to create an App

	* python manage.py startapp website  -> creates an app called website

* Open the folder in an editor (VsCode). Open settings.py and add 'website' under INSTALLED_APPS

* update below details under DATABASES <br/>
&ensp;'NAME': 'Tally',<br/>
        'USER': 'root',<br/>
        'PASSWORD': '1234',<br/>
        'HOST': 'localhost',<br/>
        'PORT': '3306',<br/>

* connect to the database

	* create one file: touch mydb.py 
	* run the file: python mydb.py
	* I got the output "All Done!!". Also you can check the name of the database you just connected on workbench.

	* python manage.py migrate (this will create a bunch of Django tables)

---------------------End of MySQl----------------------------------

* Create a superuser

	* winpty python manage.py createsuperuser


* Run Server

  	* python manage.py runserver


------------------Django Connected Successfully!!--------------------

* Initializing Git for version control

	* git config --global user.name "Avaneeshakrishna"
	* git config --global user.email "avaneesh.shastry@gmail.com"
	* git config --global push.default matching
  	* git config --global alias.co checkout
  	* git init

* Git is now added, now you can add all your files

	* git add .
  	* git commit -am 'Initial Commit'

* Create one repository on github called 'Django CRM' and push the changes

  	* git remote add origin https://github.com/Avaneeshakrishna/Django-CRM.git
  	* git branch -M main  -> change the name of the master branch to main
  	* git push -u origin main
--------------------------------------------------------------------------------------

-----------------Django Build App---------------------------------------------------URL-->VIEW-->PAGE

*  
	* Mostly working on website folder
	* create a new path under urls.py file under dcrm folder to include url files. 	
	* create urls.py file under website folder, create one Home page
	* define a home page (home.html) view under views.py file
	* create a home.html file under /website/template/home.html
	* "base.html contains all the codes that goes on every page"
	* created navbar.html, home.html and used them in base.html

* ----------------Django Login Users--------------------------

	* We use the Django Authentication system which makes it more easy.
	* Admin Login:
		Username: root
		Password: *********
*  Create migration

	* python manage.py makemigrations

	* This creates migration folder and creates one file which contains data from models.py and creates a migration

	* Now push this migration to the MySQL Database
	
	* python manage.py migrate 
