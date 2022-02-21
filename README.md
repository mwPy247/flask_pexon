# A basic flask API

## Installation

To build the image run:
`docker build -t flask_api .`

Run unittests:
`docker run --rm --name flask_api_test flask_api python -m unittest`

To start the container run:
`docker run -p 8000:8000 -it --rm --name flask_api -v db:/app/db flask_api python app.py`
Note that the -v option is important here to ensure that data persists if the container has to be restarted.

Delete the database:
`docker volume rm -f db`

## Access API from local browser

The app can then be accessed from http://localhost:8000/ inside your local browser.
To read the docs go to http://localhost:8000/apidocs/
