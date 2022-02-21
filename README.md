# A basic flask API

## Installation

To build the image run:
docker build -t flask_api .

To start the container run:
docker run -p 8000:8000 -it --rm --name flask_api -v /app/db flask_api
Note that the -v option is important here to ensure that data persists if the container has to be restarted.

## Access API from local browser

The app can then be accessed from http://localhost:8000/ inside your local browser.
To read the docs go to http://localhost:8000/apidocs/