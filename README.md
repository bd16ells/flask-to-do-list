# flask-to-do-list
Simple To-do list made with Flask &amp; SQLAlchemy

# Setup Environment

`$ virtualenv venv -p python3  `
`$ . venv/bin/activate  `
`$ pip install -r requirements.txt  `


## Initialize DB

`$ python3
Python 3.5.2 (default, Oct  8 2019, 13:06:37)   
[GCC 5.4.0 20160609] on linux  
Type "help", "copyright", "credits" or "license" for more information.  
>>> from domain import *  
>>> db.create_all()  
>>> `  

# Run app

`$ flask run  
 * Serving Flask app "main.py"  
 * Environment: production  
   WARNING: This is a development server. Do not use it in a production deployment.  
   Use a production WSGI server instead.  
 * Debug mode: off  
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)  
 `
