import unittest
import Tkinter
from demoApp import Application

class TestApplication(unittest.TestCase):

    #Tests that the application runs
    def test_application(self):
        root = Tkinter.Tk()
        app = Application(root)

#test from command line
if __name__ == '__main__':
    unittest.main()
