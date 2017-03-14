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
        """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/7/17\n
        Happens before every test"""

        self.keyOne = TEST_DATABASE.addContestant(['Alex', 'alamb25@uw.edu', ['NONE']])
        self.keyTwo = TEST_DATABASE.addContestant(['Toad', 'cranet@uw.edu', ['ONE', 'TWO']])
        TEST_DATABASE.commit()

    def tearDown(self):
        """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/7/17\n
        Happens after every test"""
        TEST_DATABASE.removeContestant( self.keyOne)
        TEST_DATABASE.removeContestant( self.keyTwo)
        TEST_DATABASE.commit()

    def test_doesUserExist(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Tests the doesUserExist function in Database.py"""

        self.assertEquals(TEST_DATABASE.doesUserExist(self.keyOne), 1, 'User does not exist')
        self.assertFalse(TEST_DATABASE.doesUserExist(12345), 'User Exist')

    def test_getContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/7/17\n
            Tests the getContestant function in Database.py"""

        temp = TEST_DATABASE.getContestant( self.keyOne)

        self.assertEquals(temp[0],  self.keyOne, 'Key failed')
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
        self.assertEqual(tmp[0][0],  self.keyOne, 'Key 1 failed')
        self.assertEqual(tmp[0][1], 'Alex', 'Name 1 failed')
        self.assertEqual(tmp[0][2], 'alamb25@uw.edu', 'Email 1 failed')
        self.assertEqual(tmp[0][3], 'NONE', 'Category 1 failed')

        self.assertEqual(tmp[1][0],  self.keyTwo, 'Key 2 failed')
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

        
        if self.keyOne < self.keyTwo:
            self.assertEqual(tmp[0], self.keyOne, 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keyTwo, 'Key 2 Failed')
        else:
            self.assertEqual(tmp[0], self.keyTwo, 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keyOne, 'Key 2 Failed')


    def test_modifyContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/8/17\n
            Tests the modifyContestant function in Database.py"""

        TEST_DATABASE.modifyContestant(self.keyOne, 'ONE/TWO')

        temp = TEST_DATABASE.getContestant(self.keyOne)
        self.assertEquals(temp[0], self.keyOne, 'Key failed')
        self.assertEquals(temp[1], 'Alex', 'Name failed')
        self.assertEquals(temp[2], 'alamb25@uw.edu', 'Email failed')

        self.assertEquals(temp[3][0], 'ONE', 'Categories 1 failed')
        self.assertEquals(temp[3][1], 'TWO', 'Categories 2 failed')

    def test_removeContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/8/17\n
            Tests the removeContestant function in Database.py"""

        TEST_DATABASE.removeContestant(self.keyOne)
        temp = TEST_DATABASE.getContestant(self.keyOne)

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

class DatabaseJudgeTest(unittest.TestCase):
    """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/13/17\n
        Tests the Judge functions in Database.py"""
    
    def setUp(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Happens before every test"""

        self.keyOne = TEST_DATABASE.addJudge(['Alex', 'alamb25@uw.edu', ['NONE']])
        self.keyTwo = TEST_DATABASE.addJudge(['Toad', 'cranet@uw.edu', ['ONE', 'TWO']])
        TEST_DATABASE.commit()

    def tearDown(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Happens after every test"""
        TEST_DATABASE.removeJudge(self.keyOne)
        TEST_DATABASE.removeJudge(self.keyTwo)
        TEST_DATABASE.commit()

    def test_doesUserExist(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Tests the doesUserExist function in Database.py"""

        self.assertEquals(TEST_DATABASE.doesUserExist(self.keyOne), 2, 'User does not exist')
        self.assertFalse(TEST_DATABASE.doesUserExist(12345), 'User Exist')

    def test_getJudge(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Tests the getJudge function in Database.py"""

        temp = TEST_DATABASE.getJudge(self.keyOne)

        self.assertEquals(temp[0], self.keyOne, 'Key failed')
        self.assertEquals(temp[1], 'Alex', 'Name failed')
        self.assertEquals(temp[2], 'alamb25@uw.edu', 'Email failed')
        self.assertEquals(temp[3][0], 'NONE', 'Categories failed')

    def  test_getAllJudges(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Tests the getAllJudges function in Database.py"""
        temp = TEST_DATABASE.getAllJudges()
        tmp = []
        i = 0
        for row in temp:
            tmp.insert(i, [row[0], row[1], row[2], ' '.join(row[3])])
            i += 1
        self.assertEqual(tmp[0][0], self.keyOne, 'Key 1 failed')
        self.assertEqual(tmp[0][1], 'Alex', 'Name 1 failed')
        self.assertEqual(tmp[0][2], 'alamb25@uw.edu', 'Email 1 failed')
        self.assertEqual(tmp[0][3], 'NONE', 'Category 1 failed')

        self.assertEqual(tmp[1][0], self.keyTwo, 'Key 2 failed')
        self.assertEqual(tmp[1][1], 'Toad', 'Name 2 failed')
        self.assertEqual(tmp[1][2], 'cranet@uw.edu', 'Email 2 failed')
        self.assertEqual(tmp[1][3], 'ONE TWO', 'Category 2 failed')

    def test_getAllJudgesIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Tests the getAllJudgesIDs function in Database.py"""

        temp = TEST_DATABASE.getAllJudgesUserIDs()
        tmp = []
        for row in temp:
            tmp.append(row)

        if self.keyOne < self.keyTwo:
            self.assertEqual(tmp[0], self.keyOne, 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keyTwo, 'Key 2 Failed')
        else:
            self.assertEqual(tmp[0], self.keyTwo, 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keyOne, 'Key 2 Failed')


    def test_modifyContestant(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Tests the modifyJudges function in Database.py"""

        TEST_DATABASE.modifyJudge(self.keyOne, 'ONE/TWO')

        temp = TEST_DATABASE.getJudge(self.keyOne)
        self.assertEquals(temp[0], self.keyOne, 'Key failed')
        self.assertEquals(temp[1], 'Alex', 'Name failed')
        self.assertEquals(temp[2], 'alamb25@uw.edu', 'Email failed')

        self.assertEquals(temp[3][0], 'ONE', 'Categories 1 failed')
        self.assertEquals(temp[3][1], 'TWO', 'Categories 2 failed')

    def test_removeJudge(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Tests the removeJudge function in Database.py"""

        TEST_DATABASE.removeJudge(self.keyOne)
        temp = TEST_DATABASE.getJudge(self.keyOne)

        self.assertEqual(temp, [], 'remove failed')

    def test_uniqueKeys(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Tests the unqiue key creates 10000 Judges to ensure conflicts"""

        uniqueDB = Database('Many.db')

        for i in range(10000):
            self.assertTrue(uniqueDB.addJudge(['', '', '']), 'Failed')

        #close and get rid of database
        uniqueDB.closeDB()
        try:
            os.remove('Many.db')
        except OSError:
            pass

class DatabaseAdminTest(unittest.TestCase):
    """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/14/17\n
        Tests the Admin functions in Database.py"""
   
    def setUp(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Happens before every test"""
        TEST_DATABASE.addAdmin([1, 'Alex', 'alamb25@uw.edu'])
        TEST_DATABASE.addAdmin([2, 'Toad', 'cranet@uw.edu'])
        TEST_DATABASE.commit()


    def tearDown(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/13/17\n
            Happens after every test"""
        TEST_DATABASE.removeAdmin(1)
        TEST_DATABASE.removeAdmin(2)
        TEST_DATABASE.commit()

    def test_doesUserExist(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the doesUserExist function for Admins in Database.py"""

        self.assertEquals(TEST_DATABASE.doesUserExist(1), 3, 'User does not exist')
        self.assertFalse(TEST_DATABASE.doesUserExist(12345), 'User Exist')

    def test_getAdmin(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the getAdmin function in Database.py"""

        temp = TEST_DATABASE.getAdmin(1)

        self.assertEquals(temp[0], 1, 'Key failed')
        self.assertEquals(temp[1], 'Alex', 'Name failed')
        self.assertEquals(temp[2], 'alamb25@uw.edu', 'Email failed')


    def  test_getAllAdminss(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the getAllAdmins function in Database.py"""
        temp = TEST_DATABASE.getAllAdmins()
        tmp = []
        i = 0
        for row in temp:
            tmp.insert(i, [row[0], row[1], row[2]])
            i += 1
        self.assertEqual(tmp[0][0], 1, 'Key 1 failed')
        self.assertEqual(tmp[0][1], 'Alex', 'Name 1 failed')
        self.assertEqual(tmp[0][2], 'alamb25@uw.edu', 'Email 1 failed')

        self.assertEqual(tmp[1][0], 2, 'Key 2 failed')
        self.assertEqual(tmp[1][1], 'Toad', 'Name 2 failed')
        self.assertEqual(tmp[1][2], 'cranet@uw.edu', 'Email 2 failed')

    def test_getAllAdminsIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the getAllAdminsIDs function in Database.py"""

        temp = TEST_DATABASE.getAllAdminsUserIDs()
        tmp = []
        for row in temp:
            tmp.append(row)


        self.assertEqual(tmp[0], 1, 'Key 1 Failed')
        self.assertEqual(tmp[1], 2, 'Key 2 Failed')


    def test_removeAdmin(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the removeAdmin function in Database.py"""

        TEST_DATABASE.removeAdmin(1)
        temp = TEST_DATABASE.getAdmin(1)

        self.assertEqual(temp, [], 'remove failed')

class DatabaseCategoryTest(unittest.TestCase):
    """ Author: Alex Lambert\n
        UW NetID: alamb25\n
        Date: 3/14/17\n
        Tests the Category functions in Database.py"""

    def setUp(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Happens before every test"""

        self.keyOne = TEST_DATABASE.addCategory(['Toad Contest', 'fun', '9:30am'])
        self.keyTwo = TEST_DATABASE.addCategory(['Alex Contest', 'more fun', '10:30am'])
        TEST_DATABASE.commit()

    def tearDown(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Happens after every test"""

        TEST_DATABASE.removeCategory(self.keyOne)
        TEST_DATABASE.removeCategory(self.keyTwo)
        TEST_DATABASE.commit()

    def test_getCategory(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the getCategory in Database.py"""

        temp = TEST_DATABASE.getCategory(self.keyOne)

        self.assertEquals(temp[0], self.keyOne, 'Key Failed')
        self.assertEquals(temp[1], 'Toad Contest', 'Name Failed')
        self.assertEquals(temp[2], 'fun', 'Description Failed')
        self.assertEquals(temp[3], '9:30am', 'Time Failed')

    def test_getAllCategories(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the getAllCategories in Database.py"""

        temp = TEST_DATABASE.getAllCategories()
        tmp = []
        i = 0
        for row in temp:
            tmp.insert(i, [row[0], row[1], row[2], ' '.join(row[3])])
            i += 1
        self.assertEqual(tmp[0][0], self.keyOne, 'Key 1 failed')
        self.assertEqual(tmp[0][1], 'Toad Contest', 'Name 1 failed')
        self.assertEqual(tmp[0][2], 'fun', 'Description 1 failed')
        self.assertEqual(tmp[0][3], '9 : 3 0 a m', tmp[0][3])

        self.assertEqual(tmp[1][0], self.keyTwo, 'Key 2 failed')
        self.assertEqual(tmp[1][1], 'Alex Contest', 'Name 2 failed')
        self.assertEqual(tmp[1][2], 'more fun', 'Description 2 failed')
        self.assertEqual(tmp[1][3], '1 0 : 3 0 a m', tmp[1][3])

    def test_getAllCategoriesIDs(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the getAllCategoriesIDs function in Database.py"""

        temp = TEST_DATABASE.getAllCategoriesIDs()
        tmp = []
        for row in temp:
            tmp.append(row)

        if self.keyOne < self.keyTwo:
            self.assertEqual(tmp[0], self.keyOne, 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keyTwo, 'Key 2 Failed')
        else:
            self.assertEqual(tmp[0], self.keyTwo, 'Key 1 Failed')
            self.assertEqual(tmp[1], self.keyOne, 'Key 2 Failed')

    def test_modifyCategory(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the modifyCategory function in Database.py"""

        TEST_DATABASE.modifyCategory(self.keyOne, ['New Category', 'The Best One', '4:30 pm'])

        temp = TEST_DATABASE.getCategory(self.keyOne)

        self.assertEquals(temp[1], 'New Category', 'Name Failed')
        self.assertEquals(temp[2], 'The Best One', 'Description Failed')
        self.assertEquals(temp[3], '4:30 pm', temp[3])

    
    def test_removeCategory(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the removeCategory function in Database.py"""
        
        TEST_DATABASE.removeCategory(self.keyOne)
        temp = TEST_DATABASE.getCategory(self.keyOne)

        self.assertEqual(temp, [], 'Removed failed')

    def test_uniqueKeys(self):
        """ Author: Alex Lambert\n
            UW NetID: alamb25\n
            Date: 3/14/17\n
            Tests the unqiue key creates 10000 Categories to ensure conflicts"""

        uniqueDB = Database('Many.db')

        for i in range(10000):
            self.assertTrue(uniqueDB.addCategory(['', '', '']), 'Failed')

        #close and get rid of database
        uniqueDB.closeDB()
        try:
            os.remove('Many.db')
        except OSError:
            pass

if __name__ == '__main__':
    unittest.main()
