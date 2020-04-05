# FullThrottle

## Setup

1. The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/tejendrasingh/FullThrottle.git
$ cd FullThrottle
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
```

3. Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:

4. Create database tables:
```sh
(env)$ python manage.py makemigrations core
(env)$ python manage.py migrate
```
5. Insert dummy data using custom management command:
```sh
(env)$ python manage.py populatedata core/management/commands/users.csv core/management/commands/periods.csv
```

## Starting the web server

1. Run python application:
```sh
(env)$ python manage.py runserver
```
Or
```sh
(env)$ python manage.py runserver 0.0.0.0:8080
```

## Test the API using Curl Command:

1. Curl command to show all users detail:
```sh
(home)$ curl -X GET 'http://127.0.0.1:8000/api/v1/users'
```

## Response:

{
  "ok": true,
  "members": [{
    "id": "W012A3CDE",
    "real_name": "Egon Spengler",
    "tz": "America/Los_Angeles",
    "activity_periods": [{
      "start_time": "Feb 01 2020 01:33PM",
      "end_time": "Feb 01 2020 01:54PM"
    }, {
      "start_time": "Mar 01 2020 11:11AM",
      "end_time": "Mar 01 2020 02:00PM"
    }, {
      "start_time": "Mar 16 2020 05:33PM",
      "end_time": "Mar 16 2020 08:02PM"
    }]
  }, {
    "id": "W07QCRPA4",
    "real_name": "Glinda Southgood",
    "tz": "Asia/Kolkata",
    "activity_periods": [{
      "start_time": "Feb 01 2020 01:33PM",
      "end_time": "Feb 01 2020 01:54PM"
    }, {
      "start_time": "Mar 01 2020 11:11AM",
      "end_time": "Mar 01 2020 02:00PM"
    }, {
      "start_time": "Mar 16 2020 05:33PM",
      "end_time": "Mar 16 2020 08:02PM"
    }]
  }]
}


Curl command to show Specific user detail using user_id:
```sh
(home)$ curl -X GET 'http://127.0.0.1:8000/api/v1/users/W012A3CDE'
```
## Response:

{
  "ok": true,
  "members": [{
    "id": "W012A3CDE",
    "real_name": "Egon Spengler",
    "tz": "America/Los_Angeles",
    "activity_periods": [{
      "start_time": "Feb 01 2020 01:33PM",
      "end_time": "Feb 01 2020 01:54PM"
    }, {
      "start_time": "Mar 01 2020 11:11AM",
      "end_time": "Mar 01 2020 02:00PM"
    }, {
      "start_time": "Mar 16 2020 05:33PM",
      "end_time": "Mar 16 2020 08:02PM"
    }]
  }]
}

