# TheBlog
## Introduction
TheBlog is a website built in Django using Python, Bootstrap CSS and HTML. It enables users to create posts with other users from around the world. It is targetted towards users who enjoy having a discussions about different topics and would like to share their ideas with others. Users have the ability to create categories, create posts, delete posts, edit posts, and create their own profile. They can upload images for use on their posts or on their profile, link their personal social media accounts and websites, and like other users posts.

This is the fourth project for the Code Institute Diploma in Software Development.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, and Full CRUD functionality for Posts, Comments, Categories, and User Profiles.

<img src = 'media/images/deployment/Laptop1440.jpg' alt = "Homepage of the website"> </img>

## Table of Contents
## Table of Contents
* [User Experience Design (UX)](#UX)
    * [The Strategy Plane](#The-Strategy-Plane)
        * [Site Goals](#Site-Goals)
        * [User Story](#User-Story)
    * [The Scope Plane](#The-Scope-Plane)
    * [The Skeleton Plane](#The-Skeleton-Plane)
        * [Wireframes](#Wireframe-mockups)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### The Strategy Plane
*  TheBlog is intended to be a friendly community site for users to create and share their thoughts and discussions with others. Users will also be able to find posts created by other users from around the world. 
##### The Sites Ideal User
* Anyone looking to share their thoughts on different subjects with others
* Someone looking to expand their knowledge
* Someone looking for inspiration for new things to try
* Someone looking build their social media following

#### Site Goals

* To provide users with a place to find new discussions
* To provide users with a place to share their own discussions

#### User Story

10 US were created which were then further developed into 18 User Stories. The details on each User story, [here](https://github.com/users/Jnaesi/projects/1/views/1)

1. Initial Django setup 
2. Setup project databases and deployment
3. Add blog posts to the django webpage
4. Style the blog with Bootstrap
5. Update and Edit blog posts
6. Add Delete a blog post function
7. Order blog posts by date
8. Blog categories pages
9. site owner objectives 
10. Create User logins/registration with authentications
etc.

#### Site Goals
* To provide users with a fun and simple layout 
* To ensure the site is fully accessible on desktop and touch enabled devices
* To ensure the site is fully compliant with keyboard commands and screen readers

### The Scope Plane

**Features planned:**

* User Profile - Create, Read, Update and Delete
* Posts - Users can create, read, update and delete their own Posts
* Other Users Posts - Users can read, like, and comment
* Profiles - Users can read other users profiles
* Users can login to their account, change their password or their names.
* Users can reset their password if they forget it
* Users can logout of their account
* Users need to be registered and logged in to add a post and like functionality.
* Responsive Design - the site needs to be fully responsive to cover the wide variety of devices users may use to access the site
#### The Skeleton Plane
I used Adobe Photoshop to produce wireframes of how the site would look across different devices.

<img src="media/images/deployment/wireframe_mockup.jpg" alt="drawing" width="800" height="600"/>


# Features
* Common Features
The site is designed with a central layout that the HTML inserts the relevant CSS into.

* Future Features
There will be an form added where you can order food that has different delivery options.

#### Main Page
<img src = 'media/images/deployment/Laptop1440.jpg' alt = "Homepage of the website" width=400> </img>

#### Add Category Page
<img src = 'media/images/deployment/AddCategoryPage.jpg' alt = "Second part" width=400> </img>

#### Add Post Page
<img src = 'media/images/deployment/AddPostPage.jpg' alt = "form" width=400> </img>

#### Comment Page

<img src = 'media/images/deployment/CommentPage.jpg' alt = "form2" width=400> </img>

#### Edit Profile Page

<img src = 'media/images/deployment/EditProfilePage.jpg' alt = "form2" width=400> </img>

#### Update Post Page

<img src = 'media/images/deployment/UpdatePostPage.jpg' alt = "form2" width=400> </img>


#### Validator Testing
* HTML
  * No errors were returned when passing through the official W3C Validator.

* Lighthouse 
  * The lighthouse report gave a great score of 97
  
  <img src="media/images/deployment/97preform.jpg" alt="Refresh" width="500"/>

#### Notable Bugs
No notable bugs during testing.

## Credits

1. codeinsitute.com
2. stackoverflow.com
3. w3schools.com
4. getbootstrap.com
### Wireframe
* MockFlow - https://www.mockflow.com

#### Technologies Used

* Python
    * The following python modules were used on this project:
      * asgiref==3.5.2
      * cloudinary==1.30.0
      * dj-database-url==0.5.0
      * dj3-cloudinary-storage==0.0.6
      * Django==3.2.16
      * django-ckeditor==6.5.1
      * django-js-asset==2.0.0
      * gunicorn==20.1.0
      * Pillow==9.3.0
      * psycopg2==2.9.5
      * pytz==2022.5
      * sqlparse==0.4.3

#### Resources Used

* The Django documentation was used extensively during development of this project
* The Cloudinary documentation was used extensively during development to setup the configuration between django and the cloudinary apis
* The Code Institute reference material was used as a general reference for things that I had previously done during the course.
* All other resources used are referenced where appropriate.

### Deployment

The site was deployed via Heroku, and the live link can be found here - [TheBLOG](https://theblogpp4.herokuapp.com/)

### Project Deployment

To deploy the project through Heroku I followed these steps:
* Sign up / Log in to [Heroku](https://www.heroku.com/)
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered theblogpp4 and select a suitable region, then select create app. The name for the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
* Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
* Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
* insert the line if os.path.isfile("env.py"): import env
* remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
* replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection
* Navigate in a browser to cloudinary, log in, or create an account and log in. 
* From the dashboard - copy the CLOUDINARY_URL to the clipboard
* in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
* this key value pair must be removed prior to final deployment
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
* in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
* Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

## Github Deployment

* The site was deployed to GitHub pages. The steps to deploy are as follows:
  * In the GitHub repository, navigate to the settings tab
  * Select the pages link from the setting menu on the left hand side 
  * Under the GitHub Pages from the source section drop-down menu, select the master branch 
  * One the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 


### Acknowledgements
I'd like to thank the students and community on slack that helped me through Javascript and the incredible learning materials on code institute.