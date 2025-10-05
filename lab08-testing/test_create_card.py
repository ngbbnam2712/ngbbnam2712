import unittest
from unittest.mock import MagicMock

# Hàm mô phỏng create_card
def create_card(title, description, list_id, user_id, db):
    if not title:
        raise ValueError("Title cannot be empty")

    if not db.list_exists(list_id):
        raise LookupError("List not found")

    if not db.user_exists(user_id):
        raise LookupError("User not found")

    if len(description) > 255:
        raise ValueError("Description too long")

    return db.insert_card(title, description, list_id, user_id)


class TestCreateCard(unittest.TestCase):

    def setUp(self):
        # Tạo mock DB
        self.mock_db = MagicMock()
        self.mock_db.list_exists.return_value = True
        self.mock_db.user_exists.return_value = True
        self.mock_db.insert_card.return_value = 1

    def test_create_card_success(self):
        card_id = create_card("Task 1", "Desc", 1, 1, self.mock_db)
        self.assertEqual(card_id, 1)

    def test_create_card_empty_title(self):
        with self.assertRaises(ValueError):
            create_card("", "Desc", 1, 1, self.mock_db)

    def test_create_card_list_not_found(self):
        self.mock_db.list_exists.return_value = False
        with self.assertRaises(LookupError):
            create_card("Task 2", "Desc", 99, 1, self.mock_db)

    def test_create_card_user_not_found(self):
        self.mock_db.user_exists.return_value = False
        with self.assertRaises(LookupError):
            create_card("Task 3", "Desc", 1, 99, self.mock_db)

    def test_create_card_description_too_long(self):
        long_desc = "x" * 300
        with self.assertRaises(ValueError):
            create_card("Task 4", long_desc, 1, 1, self.mock_db)


if __name__ == "__main__":
    unittest.main()
