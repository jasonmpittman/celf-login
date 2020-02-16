# Celf-Login
A password authentication demo for the CELF built using the Python Flask stack.

# Getting Started
Clone this repository to get started. 

    git clone celf-login repo

Then, you'll need the virtual environment component for Python.

    install python3-venv


In the repository directory, we can run:

    python3 -m venv venv

This creates a new virtual environment named *venv*. Then we have to activate it using the following command. Note: the shell prompt should change to indicate you are *in* the virtual environment.

    source venv/bin/activate

Once you have the Python virtual environment running, you need to install three modules.

    'pip install flask'
    'pip install flask_wtf'
    'pip install python-dotenv'

# Run the demo
In your shell, execute 
    flask run

# Access the demo
Point a web browser to: http:hostname.domain.suffix/login
