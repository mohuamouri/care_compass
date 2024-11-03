<div align="center"><h1>  CRUD API  </h1> </div>

## Setup

##### Step 1 - The first thing to do is to clone the repository:

```sh
git clone https://github.com/sajibsd013/care_compass.git
```

##### Step 2 - Create a virtual environment and activate it:

```sh
python -m venv myenv
myenv\Scripts\activate
```

##### Step 3 -Then install the dependencies:

```sh
cd care_compass
pip install -r requirements.txt
```

##### Step 4 - Change database setting from setting.py as follows and start database server:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'care_compass_db', #Your Database Name
        'USER': 'root', #database user with remote access privilege
        'PASSWORD': '', #password
        'HOST': '127.0.0.1', #server ip address
        'PORT': '3306', #PORT
    }
}
```

##### Step 5 - create database:

```sh
python manage.py migrate
```

##### Step 6 - create admin username and password:

```sh
python manage.py createsuperuser
```

##### Step 7 - Then run your project:

```sh
python manage.py runserver
```
