#!/usr/bin/env python3.6
from users import Users
from credentials import Credentials
def create_user(email,username,password):
    '''
    Function to create a new user
    '''
    new_user = Users(email,username,password)
    return new_user
def create_credential(app_name,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(app_name,password)
    return new_credential

def save_user(user):
    '''
    Function to save new user
    '''
    user.save_user()

def save_credential(credential):
    '''
    Function to save new credential
    '''
    credential.save_credential()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return user.find_by_username(username)

def find_credential(app_name):
    '''
    Function that finds a credential by app_name and returns the credential
    '''
    return Credentials.find_by_app_name(app_name)

def check_existing_user(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return Users.user_exist(username)

def check_existing_credential(app_name):
    '''
    Function that check if a credential exists with that app_name and return a Boolean
    '''
    return Credentials.credential_exist(app_name)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return Users.display_user()

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credential()

def main():
    print("Hello Welcome to your users list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    print("New user")
    print("-"*10)

    print ("email ....")
    email = input()

    print("username ...")
    username = input()

    print("password ...")
    password = input()

    while True:
                    print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, del -delete a credential, ex -exit the credentials list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Credential")
                            print("-"*10)

                            print ("app_name ....")
                            app_name = input()

                            print("password ...")
                            password = input()

                    # print("now let procceed to login to our account")
                    # print('\n')

                    # print("enter your username (the username must be the same as the first username you entered previously ):")
                    # print('\n')

                    # print("enter username")
                    # login_name=input()

                    # print("enter password")
                    # passw=input()
    
                    # if fi_password==passw and user_name==login_name:
                    #     print("successfully logged in")
                    #     print('\n')
                    # else:
                    #     print(f"password: {passw} or name: {login_name} incorrect. Next time , Please enter password correctly.")  
                    #     sys.exit()       


                            save_credential(create_credential(app_name,password)) # create and save new credential
                            print ('\n')
                            print(f"New Credential {app_name} {password} created!!")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_credential():
                                    print("Here is a list of all your credentials")
                                    print('\n')

                                    for credential in display_credential():
                                            print(f"{credential.app_name} {credential.password} .....")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any credential saved yet!")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the appliacation name you want to search for")

                            search_application = input()
                            if check_existing_credential(search_application):
                                    search_credential = find_credential(search_application)
                                    print(f"{search_credential.password} {search_credential.app_name}")
                                    print('-' * 20)

                                    print(f"app_name.......{search_credential.app_name}")
                                    print(f"password.......{search_credential.password}")
                            else:
                                    print("That credential does not exist")

                    elif short_code == 'del':
                            print("enter the name of credential you want to delete")
                            search_application=input()

                            if check_existing_credential(search_application):
                                    Credential =find_credential(search_application) 
                                    del_credential(Credential)
                                    print(f"{Credential.app_name} deleted")
                                    print('\n')

                                    print("credential and password deleted")
                            else:
                                    print("account name does not exist")  

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()