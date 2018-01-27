#!/usr/bin/python

'''
@joseanavarrete
janavarretecristino@gmail.com

Exercise to parse users from a JSON and add them to an invitation list in case
they fit the conditions (having an id and a distance < 100 km to a position)
'''


import json
from src.user_selector import UserSelector
from src.user import User


def main():
    user_selector = UserSelector()
    with open('customers.json', 'r') as customer_file:
        for customer in customer_file.readlines():
            try:
                user = User.from_dict(json.loads(customer.rstrip()))
                user_selector.append(user)
            except:
                print('{} could not be converted to a user'.format(customer))
    lucky_users = user_selector.sort_by_user_id()

    for user in lucky_users:
        print(user)

if __name__ == '__main__':
    main()
