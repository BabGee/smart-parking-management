# smart-parking-management

## Hosted at 

https://babgee.pythonanywhere.com/

**smart parking management** is a web application written in Python 3 and using Django framework.It deals with the management of parking spaces indicating the booked spaces and empty ones.
It enables users to Register and Login.
It enables logged in users to book for a parking spot from different parking zones, get parking receipt with parking details and checkout from a parking spot.
Admins are able to create parking zones indicating the number of parking spots available.
Admins are able to view parking details of all users.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See installing instructions for notes on how to deploy the project on a live system.



### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3.9
* Django 3.1.6
* pipenv (not mandatory but highly recommended)

### Installing
Get a local copy of the project directory by cloning "smart-parking-management" from github. `https://github.com/BabGee/smart-parking-management.git`
N/B: I used SSH clone

I use pipenv for developing this project so I recommend you to create a virtual environment and activate it, `python3 -m pipenv shell`  and to install the requirements `python3 -m pip install -r requirements.txt`.

Then follow these steps:
1. Move to root folder `cd parking_management`
2. Create a `.env` file in the root folder, provide the required database information  to the `.env` file (.env.example file is provided to help set this information)
3. Create the tables with the django command line `python manage.py makemigrations` then `python manage.py migrate`
4. Create your admin log in credentials `python manage.py createsuperuser` and add parking zones details.
5. Finally, run the django server `python manage.py runserver `


## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language
* [Django](https://www.djangoproject.com/) - Web framework 


## Versioning
I use exclusively Github

## License

This is an open source project not under any particular license.
However framework, packages and libraries used are on their own licenses. Be aware of this if you intend to use part of this project for your own project.
