import unittest
from myapp import env

class TestNewUser(unittest.TestCase):
    
    def test_get_name(self):
        template = env.get_template('user/new.html')
        assert 'ahlev' in template.render(name='ahlev')
