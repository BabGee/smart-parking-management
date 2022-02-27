# smart-parking-management

## Hosted at 

https://babgee.pythonanywhere.com/

Smart parking management is a web-based system with the following functionalities.
1. Register new users.
2. Log in registered users.
3. Logged in users can book for a parking spot from different parking zones, get parking receipt with parking details and checkout from a parking spot.
4. Admins can create parking zones indicating the number of parking spots available.
5. Admin can view parking details of all users.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See installing instructions for notes on how to deploy the project on a live system.

### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3
* Django 3.1.6
* pipenv (not mandatory but highly recommended)


### Installation

Get a local copy of the project directory by cloning "smart-parking-management" from github.

```bash
git clone https://github.com/BabGee/smart-parking-management.git
```

cd into the folder

```bash
cd smart-parking-management
```

The Framework, Packages and Libraries used in this project are installed in a virtual environment(Recommended); i use pipenv. Instructions on how to get pipenv [here](https://pypi.org/project/pipenv/)

```bash
python3 -m pipenv shell
```

Install the requirements

```bash
python3 -m pip install -r requirements.txt
```

Then follow these steps:
1. Move to root folder 

```bash
cd parking_management
```
2. Create a `.env` file in the root folder, provide the required database information  to the `.env` file (.env.example file is provided to help set this information). You can choose to rename the .env.example to .env

3. Create the tables with the django command line

```bash
python3 manage.py makemigrations
```
then migrate the changes
 
```bash
python3 manage.py migrate
```

Create an admin using command below and enter your preferred username, email and password.(You will use this to login django admin and create parking lots etc)
 
```bash
python3 manage.py createsuperuser
```


4. Finally, run the django server

```bash
python manage.py runserver
```

5. Access the django admin by adding ' /admin' to the url and login to create parking lots



## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language
* [Django](https://www.djangoproject.com/) - Web framework 


## Versioning
I use exclusively Github

## License

This is an open source project not under any particular license.
However framework, packages and libraries used are on their own licenses. Be aware of this if you intend to use part of this project for your own project.


