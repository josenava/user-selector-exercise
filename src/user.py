from .position import Position
from .distance_calculator import DistanceCalculator
from .user_selector import UserSelector

class User(object):
    def __init__(self, display_name, user_id, position):
        self.display_name = display_name
        self.user_id = user_id
        self.position = position
        self.distance_to_dublin = DistanceCalculator.to_dublin(position)

    def __str__(self):
        return 'name: {} -- user_id: {}'.format(self.display_name, self.user_id)

    @classmethod
    def from_dict(cls, dict_data):
        position = Position(float(dict_data['latitude']),
                            float(dict_data['longitude']))
        user = cls(dict_data['name'], dict_data['user_id'], position)

        return user

    def can_be_invited(self):
        ''' Defines whether a user can be invited or not based on the user
            having an id and a known distance
        '''
        return self.user_id is not None \
            and self.distance_to_dublin is not None \
            and self.distance_to_dublin <= UserSelector.MAX_DISTANCE_TO_INVITE
