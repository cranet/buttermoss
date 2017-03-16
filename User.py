"""User Class"""
class User(object):
    """User Class
    Author: Todd Crane\n
    UW NetID: cranet\n
    Date: 3/15/2017\n"""

    def __init__(self, name="", email="", ID=0):
        """Constructor"""
        self.name = name
        self.email = email
        self.userID = ID