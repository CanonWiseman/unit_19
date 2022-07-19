from app import app
from unittest import TestCase
from flask import session

class AppTestCase(TestCase):
    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<button>BEGIN</button>', html)

    def test_create_board(self):
        with app.test_client() as client:
            resp = client.get("/create-board")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(session['board'], session['board'])

