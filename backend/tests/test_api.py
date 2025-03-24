def test_submit_equation(self):
    response = self.client.post('/submit_equation', json={'equation': 'x^2'})
    self.assertEqual(response.status_code, 200)