#!/usr/bin/env python3.6
from user import Users
def create_user(emal,username,password):
    '''
    Function to create a new user
    '''
    new_user = Users(emal,username,password)
    return new_user