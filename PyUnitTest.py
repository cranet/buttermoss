import unittest
from demoApp import Application

class TestApplication(unittest.TestCase):

    #Tests that the application runs
    def test_application(self):
        demo_app = Application("Test")

#test from command line
if __name__ == '__main__':
    unittest.main()
