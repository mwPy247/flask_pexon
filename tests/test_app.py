"""
This is the test_app module.
It defines a BaseTest class and a TestAPI class that derives from BaseClass.
"""
from flask_testing import TestCase

from app import db, app
from db.models import Movie


class BaseTest(TestCase):
    """ The BaseTest module implements basic testing infrastructure. """

    def create_app(self):
        """
        The class configures the app with the central configuration file config.py

        :return:
        app: <class 'flask.app.Flask'> - A flask app object.
        """
        app.config.from_object('config.Test')
        return app

    def setUp(self):
        """ The method creates a movies table and inserts one dummy row. """
        db.create_all()
        db.session.add(Movie(director='example1', language='example2', title='example3'))
        db.session.commit()

    def tearDown(self):
        """ The method removes the previously inserted data. """
        db.session.remove()
        db.drop_all()


class TestAPI(BaseTest):
    """ The class provides a simple test battery for testing the app-API"""

    def test_status_hello(self):
        """ Tests the status code of route '/'. """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_msg(self):
        """ Tests the message returned on route '/' via GET. """
        response = self.client.get('/')
        self.assertEqual(b'Hello World', response.data)

    def test_movies_msg(self):
        """ Tests the message on route '/movies/ via GET. """
        response = self.client.get('/movies/')
        self.assertIn(b'example1', response.data)
        self.assertIn(b'example2', response.data)
        self.assertIn(b'example3', response.data)

    def test_movies_status_201(self):
        """ Checks the status code after a successful POST request. """
        response = self.client.post('/movies/', data=dict(director='data1',
                                                          title='data2',
                                                          language='data3'))
        self.assertEqual(response.status_code, 201)

    def test_movies_status_422_1(self):
        """ Variant1: Checks the status code of an unsuccessful POST request. """
        response = self.client.post('/movies/', data=dict(director='',
                                                          title='data2',
                                                          language='data3'))
        self.assertEqual(response.status_code, 422)

    def test_movies_status_422_2(self):
        """ Variant2: Checks the status code of an unsuccessful POST request. """
        response = self.client.post('/movies/', data=dict(director='data1',
                                                          title='',
                                                          language='data3'))
        self.assertEqual(response.status_code, 422)

    def test_movies_status_422_3(self):
        """ Variant3: Checks the status code of an unsuccessful POST request. """
        response = self.client.post('/movies/', data=dict(director='data1',
                                                          title='data2', 
                                                          language=''))
        self.assertEqual(response.status_code, 422)

    def test_movies_status_422_4(self):
        """ Variant4: Checks the status code of an unsuccessful POST request. """
        response = self.client.post('/movies/', data=dict(director='',
                                                          title='',
                                                          language=''))
        self.assertEqual(response.status_code, 422)
