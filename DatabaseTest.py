import unittest
import os
from Database import *

TEST_DATABASE = Database('Test.db')
class DatabaseContestantTest(unittest.TestCase):
    """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/7/17\n
        Tests the Contestant functions in Database.py"""

    def setUp(self):
        self.keys = []
        self.keys.insert(0, TEST_DATABASE.addContestant(['Alex', 'alamb25@uw.edu', ['NONE']]))
        self.keys.insert(1, TEST_DATABASE.addContestant(['Toad', 'cranet@uw.edu', ['ONE', 'TWO']]))
        TEST_DATABASE.commit()

    def tearDown(self):
        TEST_DATABASE.removeContestant(self.keys[0])
        TEST_DATABASE.removeContestant(self.keys[1])
        TEST_DATABASE.commit()


    def test_getContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Tests the getContestant function in Database.py"""

        temp = TEST_DATABASE.getContestant(self.keys[0])

        self.assertEquals(temp[0], self.keys[0], 'Key failed')
        self.assertEquals(temp[1], 'Alex', 'Name failed')
        self.assertEquals(temp[2], 'alamb25@uw.edu', 'Email failed')
        self.assertEquals(temp[3][0], 'NONE', 'Categories failed')

    def test_getAllContestants(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Tests the getAllContestants function in Database.py"""

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
            Tests the getAllContestantsIDs function in Database.py"""

        temp = TEST_DATABASE.getAllContestantUserIDs()
        tmp = []
        for row in temp:
            tmp.append(row)

        if self.keys[0] < self.keys[1]:
            self.assertEqual(tmp[0], self.keys[0], 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keys[1], 'Key 2 Failed')
        else:
            self.assertEqual(tmp[0], self.keys[1], 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keys[0], 'Key 2 Failed')

    def test_modifyContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/8/17\n
            Tests the modifyContestant function in Database.py"""

        TEST_DATABASE.modifyContestant(self.keys[0], 'ONE/TWO')

        temp = TEST_DATABASE.getContestant(self.keys[0])
        self.assertEquals(temp[0], self.keys[0], 'Key failed')
        self.assertEquals(temp[1], 'Alex', 'Name failed')
        self.assertEquals(temp[2], 'alamb25@uw.edu', 'Email failed')

        self.assertEquals(temp[3][0], 'ONE', 'Categories 1 failed')
        self.assertEquals(temp[3][1], 'TWO', 'Categories 2 failed')

    def test_removeContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/8/17\n
            Tests the removeContestant function in Database.py"""

        TEST_DATABASE.removeContestant(self.keys[0])
        temp = TEST_DATABASE.getContestant(self.keys[0])

        self.assertEqual(temp, [], 'remove failed')

    def test_uniqueKeys(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/8/17\n
            Tests the unqiue key creates 10000 contestants to ensure conflicts"""

        uniqueDB = Database('Many.db')

        for i in range(10000):
            self.assertTrue(uniqueDB.addContestant(['', '', '']), 'Failed')

        #close and get rid of database
        uniqueDB.closeDB()
        try:
            os.remove('Many.db')
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
