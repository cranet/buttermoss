"""User Class"""
class User(object):
    """User Class"""

    def __init__(self, name, email, ID):
        """Constructor"""
        self.name = name
        self.email = email
        self.userID = ID

        #Generate unique ID
        #self.userID = self.generateID()
        #print self.userID

    '''
    def generateID(self):
        """Generates a unique 5 digit user ID"""
        result = random.randint(10000, 99999)
        #print result
        return result
        '''