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