class Credentials: 
    Credentials_list
     def __init__(self, app_name, password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            app_name: New user application  name.
            password: New user application's password.
        '''
        self.app_name = app_name
        self.password = password
