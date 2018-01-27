class UserSelector(object):
    ''' Will only add users to the list if they fit the condition of having
        an id and a distance less or equal than 100 kms
    '''
    MAX_DISTANCE_TO_INVITE = 100 # KMs

    def __init__(self):
        self.user_list = []

    def append(self, user):
        if user.can_be_invited():
            self.user_list.append(user)
    
    def sort_by_user_id(self):
        return sorted(self.user_list, key=lambda user: user.user_id)
