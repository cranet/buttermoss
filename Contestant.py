from User import *

"""Contestant class"""
class Contestant(User):
    """Contestant class"""

    def __init__(self):
        """Constructor"""

        #Create contestant
        self = User("Bobby", "bobbob@uderwaterbasketweaving.com")

        #Add contestant to database
        self.database.addContestant(self.userID, self.name, self.email, "")

        
        a = self.database.getContestant(self.userID)
        for x in a:
            print x

    def regCategory(self):
        """Registers contestant in chosen category"""
        pass

    def dropCategory(self):
        """Drops contestant from chosen category"""
        pass

    def requestJudge(self):
        """Marks the contestant as possible judge"""
        pass

    def uploadPicture(self):
        """Uploads contestant picture"""
        pass

"""Main"""
if __name__ == '__main__':
    test = Contestant()


