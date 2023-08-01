from unittest import TestCase
from app import app
from currency import Currency


class FlaskTests(TestCase):

    def test_start(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<input type='text' name='to'>", html)

    
    def test_submit_good(self):
        with app.test_client() as client:
            resp = client.get('/submit?frm=USD&to=usd&amount=1')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<p>The result is US$1.0</p>", html)

    
    def test_submit_bad_frm(self):
        with app.test_client() as client:
            resp = client.get('/submit?frm=abc&to=usd&amount=1', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<p class='msg'>Not a valid code: ABC</p>", html)

    
    def test_submit_bad_to(self):
        with app.test_client() as client:
            resp = client.get('/submit?frm=usd&to=abc&amount=1', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<p class='msg'>Not a valid code: ABC</p>", html)


    def test_submit_bad_amount(self):
        with app.test_client() as client:
            resp = client.get('/submit?frm=usd&to=eur&amount=', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<p class='msg'>Not a valid amount.</p>", html)


    def test_submit_bad_all(self):
        with app.test_client() as client:
            resp = client.get('/submit?frm=abc&to=xyz&amount=', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<p class='msg'>Not a valid code: ABC</p>", html)
            self.assertIn("<p class='msg'>Not a valid code: XYZ</p>", html)
            self.assertIn("<p class='msg'>Not a valid amount.</p>", html)