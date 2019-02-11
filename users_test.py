import unittest # Importing the unittest module
from users import Users # Importing the contact class

class TestUsers(unittest.TestCase):

    '''
    Test class that defines test cases for the Users class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
    
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Users("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.email,"mashleyalpha@gmail.com")
        self.assertEqual(self.new_user.username,"ashleyalpha")
        self.assertEqual(self.new_user.password,"miahmamie")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the users list
        '''
        self.new_user.save_user() # saving the new users
        self.assertEqual(len(Users.users_list),1)
    
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our users_list
            '''
            self.new_user.save_user()
            test_user = Users("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # new user
            test_user.save_user()
            self.assertEqual(len(Users.users_list),2)
#setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Users.users_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our users_list
            '''
            self.new_user.save_user()
            test_user = Users("mashleyalpha@gmail.com","ashleyalpha","miahmamie") # new user
            test_user.save_user()
            self.assertEqual(len(Users.users_list),2)


if __name__ == '__main__':
    unittest.main()