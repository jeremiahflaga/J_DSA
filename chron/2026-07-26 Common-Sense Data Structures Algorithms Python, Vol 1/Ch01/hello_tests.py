import unittest
from hello import *

class HelloTests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_should_return_hello(self):
        helloMsg = say_hello()
        self.assertEqual("hello", helloMsg)



if __name__ == '__main__':
  unittest.main()