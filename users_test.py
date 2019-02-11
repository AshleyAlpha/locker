import unittest # Importing the unittest module
from users import Users # Importing the contact class

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
 def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Contact("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.email,"mashleyalpha@gmil.com")
        self.assertEqual(self.new_user.username,"ashleyalpha")
        self.assertEqual(self.new_user.password,"miahmamie")


if __name__ == '__main__':
    unittest.main()