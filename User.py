import random

"""User Class"""
class User(object):
    """User Class"""

    """Database"""
    database = []

    def __init__(self, name, email):
        """Constructor"""
        self.name = name
        self.email = email

        #Generate unique ID
        self.userID = self.generateID()
        print self.userID

    
    def generateID(self):
        """Generates a unique 5 digit user ID"""
        result = random.randint(10000, 99999)
        print result
        return result
        #return 0
        

    def getCategories(self):
        """Database call for categories list"""
        pass


    def getJudges(self):
        """Database call for judges list"""
        pass

    def getSchedule(self):
        """Database call for schedule list"""
        pass


    def register(self):
        """New user registration"""
        pass

    """
    def uploadPicture():
        """A"""
        pass
        """

"""Main"""
if __name__ == '__main__':
    test = User("abc.com", "abc")