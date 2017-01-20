import unittest
import demoApp

class TestStringMethods(unittest.TestCase):
    
    

    def setUp(self):
        self.abc = demoApp()

    def testCreateMenuBar(self):
        assert abc.create
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        #check that s.split fails when seperator not string
        with self.assertRaises(TypeError):
            s.split(2)


"""
    #test from interpreter
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity = 2).run(suite)
"""

    #test from command line
if __name__ == '__main__':
    unittest.main()

"""
    
    #Runs before every test case
    def setUp(self):
        self.demoApp = demoApp()

    #Test default size
    def testDefaultSize(self):
        assert self.widget.size() == (50, 50), 'incorrect default size'

    #Runs after every test case
    def tearDown(self):
        print("Test completed")

    def test_about(self):
        self.assertEqual(1, 1, "hi")
        
"""
