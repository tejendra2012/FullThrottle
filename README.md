# FullThrottle

1. First Clone the GitHub Repository:


2. cd FullThrottle

3. Create python virtual envirnment with python3.

  virtualenv -p /usr/bin/python3 <virtual-env-name>

4. Activate virtual envirnment.

  source <virtual-env-name>/bin/activate

5. Install django requirment package.

  pip install requirments.txt

6. Create model tables.

  python manage.py makemigrations core

  python manage.py migrate

7.  Insert dummy data using custom management command

  python manage.py populatedata

8. Run python application.

  python manage.py runserver

9. Show all users details using these Curl command.

  curl -X GET 'http://127.0.0.1:8000/api/v1/users'

10. show specific user details with user_id using these Curl command.

  curl - X GET 'http://127.0.0.1:8000/api/v1/users/W012A3CDE'

