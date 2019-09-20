# Welcome to IEXApp

A simple stock exchange application

Resource Links
- [Hosted Application](https://iexapp.herokuapp.com/)
- [Postman Documentation](https://documenter.getpostman.com/view/2846783/SVmyQwxE)


## Description

This is a simple stock exchange REST API that allows users to access the following features

- Login
- Register
- Get list of supported stock symbols
- Check the latest price for a stock
- Purchase shares on the application
- Sell shares on the application
- See previously purchased stocks
- See transaction history
- Deposit into their account wallet


## General Notes

The wallet deposit feature is just to show how the amount a user have with us on the platform affects the way they purchase shares. Hence, the payment gateway layer was not implemented.

Only the symbols for `Apple (aapl)` and `Uber (uber)` are supported on the platform, as these are the only two seeded into the database. This means that any other symbol used will cause an error message to be returned.


## Technologies

- Flask
- SQLAlchemy
- Gunicorn
- PIP


## Setup development environment

The application is a flask application which depends on Werkzeug python toolkit and Jinja2 template engine. The database abstraction and ORM library used is SQLAlchemy.

To setup the development environment, follow the below steps

```bash

# Clone the repository and change directory into it

$ git clone https://github.com/abdulfataiaka/iexapp.git

$ cd iexapp


# Install virtualenv using pip and create a virtual environment with name `venv`
# Ensure the current global python version is 3.6.x

$ pip install virtualenv

$ virtalenv venv


# Make a copy of .env.example and fill the variables below with values shared

SECRET_KEY=some-random-test
DATABASE_URL=probably-a-path-to-sqlite-db-file-on-local
TEST_DATABASE_URL=database-url-for-test-environment
IEX_CLOUD_TOKEN=get-from-email-shared
IEX_CLOUD_BASEURL=https://sandbox.iexapis.com/stable


# Activate the development environment

$ source bin/init.sh


# Install dependencies

$ pip install -r requirements.txt


# Setup the database

flask db:setup --seed


# start the application

$ flask run

```


## Running tests

Test has been written using the unittest library. Run the below command from the root directory to see all test passing.

```bash

python -m unittest discover --start-directory ./test

```


## License

This is licensed for use, distribution and modification under the MIT license.


## Author

Abdulfatai Aka - `Software Engineer` - abdulfataiaka@gmail.com
