# Django-REST-Framework

A hypothetical University, Ark Academy intends to introduce a bus tracking system aimed at
providing a smoother transport experience to its staff and students. The proposed solution
involves a Django Restframework API backend server and a frontend mobile app.
To setup the university, the backend provides following APIs for its users:
- POST v1/auth/signup/ Admin can sign up using this endpoint, using username/email
and password
- POST v1/auth/login/ Login in with username and password
- POST v1/university/ create a university
- GET v1/university/ list all universities
- GET v1/university/<id>/ get university details by id
- PUT v1/university/<id>/ edit university details by id
- DELETE v1/university/<id>/ edit university details by id

You are required to develop a REST API backend using the Django REST Framework for the
above APIs.
