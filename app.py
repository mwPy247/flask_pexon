"""
The module "app" is the central entrypoint of the API.
It implements one GET-method for the path "/"
and one GET- and one POST-method for the path "/movies".
"""

from flask import Flask, Response, request, jsonify
from flask.views import MethodView
from flasgger import Swagger

from db.models import Movie, db
from log.logger import log_factory


app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Application Documentation',
    'doc_dir': './docs/'  # Setup doc folder parsed automatically by flasgger
}
app.config.from_object('config.Dev')  # Set dev-configuration
db.init_app(app)  # Initialize the app with dev-database
app.app_context().push()  # Set context
swagger = Swagger(app)  # Initialize flasgger


class HelloAPI(MethodView):
    """ A simple Flask method view class for displaying "Hello World" via GET. """

    @log_factory(level='info')
    def get(self):
        """
        A function returning a constant.

        :return:
        str - the "Hello World" message
        """
        return "Hello World"


class MoviesAPI(MethodView):
    """ A Flask method view class to interact with the movies database via GET and POST. """

    @log_factory(level='info')
    def get(self):
        """
        The method gets all movies from the database
        and returns them as a jsonified response object.

        :return:
        <class 'flask.wrappers.Response'> - A flask response object
                                            representing the result of the query.
        """
        result = db.engine.execute("SELECT * FROM movies")
        movies = [{'id': row[0], 'director': row[1], 'language': row[2], 'title': row[3]}
                  for row in result]
        return jsonify(movies)

    @log_factory(level='info')
    def post(self):
        """
        The post method fetches form data submitted by the user.
        The method returns a response with status 422 if any of the fields is empty,
        else the method writes the data to the database and returns a response with status 201.

        :return:
        <class 'flask.wrappers.Response'> - The response object
        """
        director = request.form['director']
        language = request.form['language']
        title = request.form['title']

        data = director, language, title
        if not all(item for item in data):
            return Response('Please provide values for all fields.', status=422)

        table_row = Movie(director=director, language=language, title=title)
        db.session.add(table_row)
        db.session.commit()

        return Response(f'Movie {title} inserted successfully',
                        status=201, mimetype="application/json")


app.add_url_rule('/movies/', view_func=MoviesAPI.as_view('movies'), methods=['GET', 'POST'])
app.add_url_rule('/', view_func=HelloAPI.as_view('root'), methods=['GET'])


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=8000)
