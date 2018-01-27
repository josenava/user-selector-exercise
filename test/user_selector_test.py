import unittest
from unittest.mock import patch

from src.user_selector import UserSelector
from src.user import User

class UserSelectorTest(unittest.TestCase):
    @patch('src.user')
    def test_user_not_fitting_condition_is_not_appended(self, mock_user):
        mock_user.can_be_invited.return_value = False
        user_selector = UserSelector()
        user_selector.append(mock_user)

        self.assertEqual(len(user_selector.user_list), 0)

    @patch('src.user')
    def test_user_fitting_condition_is_appended(self, MockUser):
        mock_user = MockUser()
        mock_user.can_be_invited.return_value = True
        user_selector = UserSelector()
        user_selector.append(mock_user)

        self.assertEqual(len(user_selector.user_list), 1)


if __name__ == '__main__':
    unittest.main()
