class Credentials: 
    credentials_list=[]
    def __init__(self, app_name, password):

        self.app_name = app_name
        self.password = password
    def save_credential(self):
        '''
        save_credential method saves credential objects into credentials_list
        '''
        Credentials.credentials_list.append(self)
        
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_app_name(cls,app_name):
        '''
        Method that takes in an app_name and returns a credential that matches that app_name.

        Args:
            app_name: app_name to search for
        Returns :
            app_name of credential that matches the app_name.
        '''

        for credential in cls.credentials_list:
            if credential.app_name == app_name:
                return credential