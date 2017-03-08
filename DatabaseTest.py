import unittest
from Database import *

TEST_DATABASE = Database()
class DatabaseContestantTest(unittest.TestCase):

    def setUp(self):
        self.keys = []
        self.keys.insert(0, TEST_DATABASE.addContestant(['Alex', 'alamb25@uw.edu', 'NONE']))
        self.keys.insert(1, TEST_DATABASE.addContestant(['Toad', 'cranet@uw.edu', 'ONE/TWO']))


    def test_getContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Tests the getContestant function in Database.py"""

        print self.keys[0]
        temp = TEST_DATABASE.getContestant(self.keys[0])

        self.assertEquals(temp[0], self.keys[0], 'Key failed')
        self.assertEquals(temp[1], 'Alex', 'Name failed')
        self.assertEquals(temp[2], 'alamb25@uw.edu', 'Email failed')
        self.assertEquals(temp[3][0], 'NONE', 'Categories failed')

    def test_getAllContestants(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Tests the getAllContestant function in Database.py"""

        temp = TEST_DATABASE.getAllContestants()
        tmp = []
        i = 0
        for row in temp:
            tmp.insert(i, [row[0], row[1], row[2], ' '.join(row[3])])
            i += 1
        self.assertEqual(tmp[0][0], self.keys[0], 'Key 1 failed')
        self.assertEqual(tmp[0][1], 'Alex', 'Name 1 failed')
        self.assertEqual(tmp[0][2], 'alamb25@uw.edu', 'Email 1 failed')
        self.assertEqual(tmp[0][3], 'NONE', 'Category 1 failed')

        self.assertEqual(tmp[1][0], self.keys[1], 'Key 2 failed')
        self.assertEqual(tmp[1][1], 'Toad', 'Name 2 failed')
        self.assertEqual(tmp[1][2], 'cranet@uw.edu', 'Email 2 failed')
        self.assertEqual(tmp[1][3], 'ONE TWO', 'Category 2 failed')
   
    def test_getAllContestantsIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Tests the getAllContestant function in Database.py"""

if __name__ == '__main__':
    unittest.main()
