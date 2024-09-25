# File: app_testing.py
import unittest
from app import app

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test that the home page loads correctly
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<iframe', response.data)
        self.assertIn(b'src="https://embed.cody.bot/9ce9590d-4bf3-4871-abcb-ec67328d42cc"', response.data)

    def test_iframe_loads(self):
        # Since iframe content is external, we can only test that the iframe is present
        response = self.app.get('/')
        self.assertIn(b'<iframe', response.data)

if __name__ == '__main__':
    unittest.main()
