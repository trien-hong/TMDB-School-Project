## Installation & Running

When you clone this repo you are missing two things, .env file and node_modules folder. In order to get this running, you will need to add a .env file in the top level directory. You are missing three things within the .env file. To get node_modules folder, in your terminal type in ```npm ci```.

1. You need an TMDB API key which you can get from [themoviedb.org](https://themoviedb.org/). Within the .env file you will add your API key as a variable of TMDB_KEY in quotes.
   * ```TMDB_KEY = "INSERT YOUR TMDB KEY HERE"```

2. To get a DATABASE_URL, you will need to first create a Heroku account from [heroku.com](https://heroku.com/).  Within your terminal login to Heroku with ```heroku login -i``` and create a Heroku app with ```heroku create```. Then inside your terminal type in ```heroku addons:create heroku-postgresql:hobby-dev -a your_app_name``` to create a remote database. Type in ```heroku config```, copy that DATABASE_URL and paste that within your .env file as a variable of DATABASE_URL in quotes.  
   * ```DATABASE_URL = "INSERT YOUR DATABASE URL HERE"```

3. Your APP_SECRET_KEY is something you can make up. Just make sure it's something fairly secure and not "123" or "password". Within the .env file you will add your secret key as a variable of APP_SECRET_KEY in quotes.
   * ```APP_SECRET_KEY = "ENTER YOUR APP SECRET KEY HERE"```

### Dependencies

Note that you will also need to install python, python-dotenv, flask, flask-login, request, psycopg2-binary, postgresql, flask-sqlalchemy, heroku cli, npm, and make sure to update node.js if you have not already.

### Running

Before you can start, your database is currently empty. You need to initialize a new database. You can do so in your terminal with these commands, ```python3```, ```from app import db```, ```import models```, and ```db.create_all()```. Your database is now initalize so CTRL+D to exit the session. Once your .env is setup, your dependencies are installed, and database initialize, within your terminal type in ```npm run build``` then ```python3 app.py``` to run the app.