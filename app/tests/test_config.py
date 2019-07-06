

import unittest

from flask_testing import TestCase
from flask import current_app

from app import create_app

app = create_app()

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.DevelopmentConfig')
        return app
    
    def test_app_is_in_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'some-confidential-string')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['DATABASE_URI'] == 'postgresql://postgres:@localhost/questioner_dev'
        )

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app
    
    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'some-confidential-string')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['DATABASE_URI'] == 'postgresql://postgres:@localhost/questioner_test'
        )

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.config.ProductionConfig')
        return app

    def test_app_is_in_production(self):
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertFalse(app.config['SECRET_KEY'] is 'some-confidential-string')
        