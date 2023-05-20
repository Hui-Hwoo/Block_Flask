# Setup the python virtual environment
# pip install virtualenv
# python3 -m venv venv
source ./venv/bin/activate

# Install all necessary library
# pip install --upgrade pip
# pip install  -r requirements.txt

# Setup the development environment
export FLASK_APP=app.py   
export FLASK_ENV=development

# Activate debug mode
export FLASK_DEBUG=1

# start the program
flask run
