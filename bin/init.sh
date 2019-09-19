# activate virtual environment
. venv/bin/activate

# adding application path to PATH environ variable
export PATH="$(pwd):${PATH}"

# set flask application environment variable
export FLASK_APP=app
export FLASK_ENV=development
